import cv2

image = cv2.imread("Flower.jpeg")

if image is None:
    print("Could not Load Image")
else:
    print("Image Load Successfully")

    cv2.putText(image,"This is flower", (50,300),cv2.FONT_HERSHEY_SIMPLEX ,1.2,(0,255,255),2)

    cv2.imshow("Adding Text Over Image" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
