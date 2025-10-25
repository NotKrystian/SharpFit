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
        image = cv2.imread('woj.jpg')
        pose_landmarks = getPose(image)
        #print(pose_landmarks)
        num = 0
        for idx, landmark in enumerate(pose_landmarks.pose_landmarks[0]):
            if num==30 :
                print(f'Landmark {idx}: {landmark}')
            if num==29 :
                print(f'Landmark {idx}: {landmark}')
            num += 1
        world = pose_landmarks.pose_world_landmarks[0]
        pose29 = np.array([world[29].x, world[29].y, world[29].z], float)
        pose30 = np.array([world[30].x, world[30].y, world[30].z], float)
        realDistance = np.linalg.norm(pose29 - pose30)
        scale = .3/realDistance
        print("scale:", scale)
        hipR = np.array([world[16].x, world[16].y,world[16].z], float)
        hipL = np.array([world[15].x, world[15].y,world[15].z], float)
        waistLength = np.linalg.norm(hipL - hipR) * scale
        print("waistLength:", waistLength)