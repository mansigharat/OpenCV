import cv2

image = cv2.imread("Flower.jpeg")

if image is None:
    print("Image not Found")
else:
    print("Image Loaded")
    resized = cv2.resize(image , (400,300))

    cv2.imshow("Original Image",image)
    cv2.imshow("Resize Image",resized)

    cv2.imwrite("resized_output.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()