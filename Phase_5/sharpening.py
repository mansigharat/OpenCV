import cv2
import numpy as np

image = cv2.imread("image.png")

sharpenKernal = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharpened = cv2.filter2D(image, -1 ,sharpenKernal)

cv2.imshow("Original image",image)
cv2.imshow("Sharpen image",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()