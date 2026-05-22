import cv2

image = cv2.imread("image.png")

blurred = cv2.medianBlur(image,5)

cv2.imshow("Original image",image)
cv2.imshow("Median Blurred",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()