import cv2
image = cv2.imread("Flower.jpeg")
if image is not None:
    h , w, c = image.shape
    print(f"Image Loaded :\nHeight: {h} \nWidthL {w}\nChannels: {c}")
else:
    print("Could not Load image")