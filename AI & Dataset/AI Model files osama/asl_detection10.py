# Import and Install Dependencies
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import trained as tk


fileName="testos6"
trainedWords = tk.testo[fileName]

# Keypoints using MP Holistic
mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

# create for each frame the corresponding landmarks (x, y, z) 
def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)      # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                       # Image is no longer writeable
    results = model.process(image)                      # Make prediction
    image.flags.writeable = True                        # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)      # COLOR COVERSION RGB 2 BGR
    return image, results

# draw style of landmarks like color, thickness and circle_radius
def draw_styled_landmarks(image, results):

    # Draw face connections
    mp_drawing.draw_landmarks(
        image,
        results.face_landmarks,
        mp_holistic.FACEMESH_CONTOURS, 
        mp_drawing.DrawingSpec(
            color=(230, 230, 230),
            thickness=1,
            circle_radius=1,
        ), 
        mp_drawing.DrawingSpec(
            color=(230, 230, 230),
            thickness=1,
            circle_radius=1,
        ),
    ) 

    # Draw pose connections
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_holistic.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(
            color=(230, 230, 230),
            thickness=2,
            circle_radius=4,
        ), 
        mp_drawing.DrawingSpec(
            color=(230, 230, 230),
            thickness=2,
            circle_radius=2,
        ),
    ) 

    # Draw left hand connections
    mp_drawing.draw_landmarks(
        image,
        results.left_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS, 
        mp_drawing.DrawingSpec(
            color=(230, 230, 230),
            thickness=2,
            circle_radius=4,
        ), 
        mp_drawing.DrawingSpec(
            color=(230, 230, 230),
            thickness=2,
            circle_radius=2,
        ),
    ),

    # Draw right hand connections  
    mp_drawing.draw_landmarks(
        image,
        results.right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS, 
        mp_drawing.DrawingSpec(
            color=(230, 230, 230),
            thickness=2,
            circle_radius=4,
        ), 
        mp_drawing.DrawingSpec(
            color=(230, 230, 230),
            thickness=2,
            circle_radius=2,
        ),
    ),     


def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z] for res in results.pose_landmarks.landmark]).reshape(-1, 3) if results.pose_landmarks else np.zeros((33, 3))
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).reshape(-1, 3) if results.face_landmarks else np.zeros((468, 3))
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).reshape(-1, 3) if results.left_hand_landmarks else np.zeros((21, 3))
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).reshape(-1, 3) if results.right_hand_landmarks else np.zeros((21, 3))
    # Check if lh and rh are both zeros
    if np.array_equal(lh, np.zeros((21, 3))) and np.array_equal(rh, np.zeros((21, 3))):
        return np.concatenate([np.zeros((33, 3)), np.zeros((468, 3)), lh, rh], axis=0)
    else:
        return np.concatenate([pose, face, lh, rh], axis=0)


# Setup Folders for Collection
actions = np.array(trainedWords)

def getPrediction(input):
    interpreter = tf.lite.Interpreter(fileName+".tflite")
    interpreter.allocate_tensors()

    # Get input and output details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Prepare input data
    input_data = np.expand_dims(input, axis=0).astype(np.float32)

    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Run inference
    interpreter.invoke()

    # Get the output
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    # Convert the list to a numpy array
    array_2d = np.array(output_data)

    # Flatten the array to convert it into a 1D array
    prediction = array_2d.flatten()

    return prediction

# 1. New detection variables
sequence = []
sentence = []
threshold = 0.10
lastSign = -1

cap = cv2.VideoCapture(0)
# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)
        
        # Draw landmarks
        draw_styled_landmarks(image, results)
        
        # 2. Prediction logic
        keypoints = extract_keypoints(results)
        keypoints = keypoints.flatten()
        if np.all(keypoints == 0):
            sequence = []                  
        sequence.append(keypoints)
        sequence = sequence[-15:]
        
        if len(sequence) == 15:

            # Check if all lists in sequence are zeros
            all_zeros = all(all(elem == 0 for elem in sublist) for sublist in sequence)

            if not all_zeros:
                
                prediction = getPrediction(sequence)

                confidence = prediction[np.argmax(prediction)]
                sign = actions[np.argmax(prediction)]
                # print('The pridection is : ', sign, 'with confidence: ', confidence)

                #3. Viz logic
                if prediction[np.argmax(prediction)] >= threshold: 
                    if lastSign == sign:
                        pass      # print('repeated sign')
                    else:
                        lastSign = sign
                        sentence.append(actions[np.argmax(prediction)])    

                if len(sentence) > 1: 
                    sentence = sentence[-1:]
                
                cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
                cv2.putText(image, ' '.join(sentence), (3,30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            else:
                sentence = [] 
                cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
                cv2.putText(image, ' '.join(sentence), (3,30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)         
        
        # Show to screen
        cv2.imshow('OpenCV Feed', image)

        # Break gracefully
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
