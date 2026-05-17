import cv2

image = cv2.imread("Flower.jpeg")

if image is None:
    print("Oops! , You image is not working")
else:
    print("Image loaded successfully")
    pt1 = (50,100)
    pt2=(300,170)
    color = (255,0,0)
    thickness = 4

    cv2.line(image , pt1, pt2,color,thickness)
    cv2.imshow("Line Drawing" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()