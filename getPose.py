import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np

model_path = 'model/pose_landmarker_heavy.task'

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE)

with PoseLandmarker.create_from_options(options) as landmarker:
    def getPose(image):
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        pose_landmarks = landmarker.detect(mp_image)
        return pose_landmarks
    if __name__ == "__main__":
        import cv2
        image = cv2.imread('test1.jpg')
        pose_landmarks = getPose(image)
        print(pose_landmarks)
        num = 0
        for idx, landmark in enumerate(pose_landmarks.pose_landmarks[0]):
            if num==30 :
                print(f'Landmark {idx}: {landmark}')
            if num==29 :
                print(f'Landmark {idx}: {landmark}')
            num += 1
        
            
