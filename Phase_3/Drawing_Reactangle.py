import cv2

image = cv2.imread("Flower.jpeg")

if image is None:
    print("Couldn't Found Image")
else:
    print("Image loaded Successfully")

    pt1 = (50,50)
    pt2 = (300,200)
    color = (0,255,0)
    thickness = 3

    cv2.rectangle(image,pt1,pt2,color,thickness)

    cv2.imshow("Rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

