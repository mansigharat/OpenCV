import cv2
image = cv2.imread("Phase 1\Flower.jpeg")
if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayScale.png", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the Image")