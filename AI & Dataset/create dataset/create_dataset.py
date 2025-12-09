# Import and Install Dependencies
import os
import cv2
import numpy as np
import mediapipe as mp

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
DATA_PATH = os.path.join('dataset') # Path for exported data, numpy arrays
actions = np.array(['non']) # Actions that we try to detect
no_sequences = 500  # Thirty videos worth of data
sequence_length = 15  # Videos are going to be 30 frames in length

# create folders for each action have 30 video
for action in actions: # for each action
    try: 
        os.makedirs(os.path.join(DATA_PATH, action)) # for each video create folder
    except:
        pass

# Collect Keypoint Values for Training and Testing
cap = cv2.VideoCapture(1)
# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    # Flag to control pause/play
    paused = False
    
    # Loop through actions
    for action in actions:
        # Loop through sequences aka videos
        for sequence in range(no_sequences):
            # Initialize an empty list to store keypoints from each frame
            all_keypoints = []
            # Loop through video length aka sequence length
            for frame_num in range(sequence_length):
                # Read feed
                ret, frame = cap.read()

                # Make detections
                image, results = mediapipe_detection(frame, holistic)

                # Draw landmarks
                draw_styled_landmarks(image, results)
                
                # Apply wait logic
                if frame_num == 0: # If you are going to start a new video
                    cv2.putText(image, 'STARTING COLLECTION', (120,200), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA) # print text (STARTING COLLECTION) on screen 
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA) # print text (Collecting frames for {action} Video Number {sequence}) on screen 

                    # Append the frame to the list
                    cv2.imshow('OpenCV Feed', image)
                    # cv2.waitKey(1000) # break 2 seconds between each video 
                else: 
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA) # print text (Collecting frames for {action} Video Number {sequence}) on screen 
            
                    # Show to screen
                    cv2.imshow('OpenCV Feed', image)
                
                # Export keypoints
                keypoints = extract_keypoints(results)

                # Append keypoints to the list
                all_keypoints.append(keypoints)

                # Break gracefully
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                elif cv2.waitKey(1) & 0xFF == ord('p'):  # Pause/Play functionality
                    paused = not paused
                
                # Pause functionality
                if paused:
                    while paused:
                        if cv2.waitKey(1) & 0xFF == ord('p'):  # Resume
                            paused = False
                            break

            # Convert the list of keypoints into a 3D numpy array
            all_keypoints_array = np.array(all_keypoints)  

            # Save the keypoints array
            npy_file = os.path.join(DATA_PATH, action, f'{str(sequence)}.npy')
            np.save(npy_file, all_keypoints_array)

# Release video capture and destroy windows
cap.release()
cv2.destroyAllWindows()
