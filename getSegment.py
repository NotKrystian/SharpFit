import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = 'model/model.tflite'
BaseOptions = mp.tasks.BaseOptions
ImageSegmenter = mp.tasks.vision.ImageSegmenter
ImageSegmenterOptions = mp.tasks.vision.ImageSegmenterOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = ImageSegmenterOptions(
    base_options=BaseOptions(model_asset_path='model/selfie_segmenter.tflite'),
    running_mode=VisionRunningMode.IMAGE,
    output_category_mask=True)
with ImageSegmenter.create_from_options(options) as segmenter:
    def getSegment(image):
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        segmentation_result = segmenter.segment(mp_image)
        return segmentation_result
    if __name__ == "__main__":
        import cv2
        image = cv2.imread('test1.jpg')
        segmentation_result = getSegment(image)
        print(segmentation_result)
        category_mask = segmentation_result.category_mask
        mask_image = category_mask.numpy_view()
        cv2.imwrite('mask.png', mask_image)
        print("Mask image saved")