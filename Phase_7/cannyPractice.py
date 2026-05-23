import cv2

image = cv2.imread("Flower.jpeg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, 50,150)

cv2.imshow("Original Image",image)
cv2.imshow("Edages",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()