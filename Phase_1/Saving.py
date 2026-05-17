import cv2
image = cv2.imread("Phase 1\Flower.jpeg")
if image is not None:
    success = cv2.imwrite("Output.png",image)
    if success:
        print("Image saved successfully as 'Output.png' ")
    else:
        print("Failed to Save an Image")
else:
    print("Error : Could not load image")