import cv2
import numpy as np

img = cv2.imread('lena.jpg')

kernel_size = 5

kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

mean_filtered = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Mean Filtered Image', mean_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
