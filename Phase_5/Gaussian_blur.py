import cv2

image = cv2.imread("Flower.jpeg")

blurred = cv2.GaussianBlur(image, (9,9),3)

cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()