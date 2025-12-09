import cv2
import threading
import numpy as np
from flask import Flask, request, jsonify
import math
import pandas as pd
import mediapipe as mp
import tensorflow as tf

app = Flask(__name__)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic

# Empty list
frames_list = []
num_frame = -1
frame_lock = threading.Lock()
sign = 0
lastSign = -1
# Kaggle Competition Data

train = pd.read_csv(r"E:\Graduation Project\dataset-asl-signs\train.csv")
parquet_file = r"E:\Graduation Project\dataset-asl-signs\train_landmark_files\2044\635217.parquet"
xyz = pd.read_parquet(parquet_file)

# open model.tflite and test prediction
interpreter = tf.lite.Interpreter(model_path=r"E:\Graduation Project\model.tflite")
prediction_fn = interpreter.get_signature_runner("serving_default")

# Add ordinally Encoded Sign (assign number to each sign name)
train['sign_ord'] = train['sign'].astype('category').cat.codes

# Dictionaries to translate sign <-> ordinal encoded sign
SIGN2ORD = train[['sign', 'sign_ord']].set_index('sign').squeeze().to_dict()
ORD2SIGN = train[['sign_ord', 'sign']].set_index('sign_ord').squeeze().to_dict()


all_Dataframes = []


def mediapipe_detection(image, model):
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable 
    return results


def create_one_Dataframe(results, frame, xyz):
    xyz_skel = xyz[['type', 'landmark_index']].drop_duplicates().reset_index(drop=True).copy()

    # Convert mediaPipe to DataFrames
    face = pd.DataFrame([[point.x, point.y, point.z] for point in results.face_landmarks.landmark],
                        columns=['x', 'y', 'z']) if results.face_landmarks else pd.DataFrame()

    pose = pd.DataFrame([[point.x, point.y, point.z] for point in results.pose_landmarks.landmark],
                        columns=['x', 'y', 'z']) if results.pose_landmarks else pd.DataFrame()

    left_hand = pd.DataFrame([[point.x, point.y, point.z] for point in results.left_hand_landmarks.landmark],
                             columns=['x', 'y', 'z']) if results.left_hand_landmarks else pd.DataFrame()

    right_hand = pd.DataFrame([[point.x, point.y, point.z] for point in results.right_hand_landmarks.landmark],
                              columns=['x', 'y', 'z']) if results.right_hand_landmarks else pd.DataFrame()

    # Create the Kaggle type format from our detection landmarks
    face = face.reset_index().rename(columns={'index': 'landmark_index'}).assign(type='face')
    right_hand = right_hand.reset_index().rename(columns={'index': 'landmark_index'}).assign(type='right_hand')
    left_hand = left_hand.reset_index().rename(columns={'index': 'landmark_index'}).assign(type='left_hand')
    pose = pose.reset_index().rename(columns={'index': 'landmark_index'}).assign(type='pose')

    landmarks = pd.concat([face, pose, left_hand, right_hand]).reset_index(drop=True)
    landmarks = xyz_skel.merge(landmarks, on=['type', 'landmark_index'], how='left')
    Dataframe = landmarks.assign(frame=frame)
    return Dataframe

def create_input_model_data(all_Dataframes):
    ROWS_PER_FRAME = 543  # number of landmarks per frame
    data_columns = ['x', 'y', 'z']

    data = pd.concat(all_Dataframes, ignore_index=True)[data_columns]
    n_frames = len(data) // ROWS_PER_FRAME
    data_np = data.to_numpy().reshape(n_frames, ROWS_PER_FRAME, len(data_columns)).astype(np.float32)
    return data_np

def display_frame():
    global num_frame
    global all_Dataframes
    global sign
    global lastSign 
    with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    ) as holistic:

        # Convert the frame bytes to a NumPy array
        frame_data = frames_list[num_frame]
        frame_np_array = np.frombuffer(frame_data, dtype=np.uint8)

        # Reshape the 1D array to a 2D grayscale image
        grayscale_image = np.reshape(frame_np_array, (480, 640))

        # Convert to 3D RGB image
        rgb_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)

        # Transpose and flip the image to display it lengthwise
        rotated_rgb_image = cv2.transpose(cv2.flip(rgb_image, 1))

        # Make detections
        results = mediapipe_detection(rotated_rgb_image, holistic)

        # create landmark dataframe
        Dataframe = create_one_Dataframe(results, len(frames_list), xyz)

        all_Dataframes.append(Dataframe)
        all_Dataframes = all_Dataframes[-3:]

        if len(all_Dataframes) == 3:
            
            model_data= create_input_model_data(all_Dataframes)
            all_Dataframes = []

            # open model.tflite and test prediction
            output = prediction_fn(inputs= model_data)
            sign = np.argmax(output["outputs"])
            pred_conf = output["outputs"][sign]
            print(ORD2SIGN[sign], pred_conf)
            if math.isnan(pred_conf) or lastSign == sign:
                return ''
            elif pred_conf > 0.20:
                lastSign = sign
                print(f'PREDICTED SIGN: {ORD2SIGN[sign]} [{sign}] with confidence {pred_conf: 0.4}')   
                return ORD2SIGN[sign]  
                       
frames = 0

@app.route('/upload', methods=['POST'])
def upload_frame():
    global frames_list
    global num_frame
    global frames
    try:
        with frame_lock:
            # Append an element to the end of the list
            frames_list.append(request.data)
            num_frame += 1  # Move to the next frame 
            frames += 1
            print(frames)
            prediction = display_frame()

            if len(frames_list) == 3:
                frames_list = []
                num_frame = -1

            return jsonify({
                "message": prediction
            })
        
    except Exception as e:
        print(f"Error processing frame: {e}")
        return "Error processing frame", 500 

if __name__ == "__main__":
    app.run(host='192.168.170.224', port=3000, debug=True)


# Release resources
cv2.destroyAllWindows()

