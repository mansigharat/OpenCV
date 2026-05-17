import cv2

image = cv2.imread("Flower.jpeg")

if image is None:
    print("Could not load image")
else:
    print("Image loaded Successfully")

    center = (100,100)
    radius = 50
    color = (0,0,255)
    thickness = -1

    cv2.circle(image,center,radius,color,thickness)

    cv2.imshow("Image Circle" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
