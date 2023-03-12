import cv2
import numpy as np
from numpy.fft import fft2, fftshift, ifft2

img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

f = fftshift(fft2(img))

D0 = 50

rows, cols = img.shape
x = np.linspace(-cols/2, cols/2, cols)
y = np.linspace(-rows/2, rows/2, rows)
xx, yy = np.meshgrid(x, y)

D = np.sqrt(xx ** 2 + yy ** 2)

H = np.zeros_like(f)
H[D <= D0] = 1

filtered_f = f * H

filtered_img = np.real(ifft2(fftshift(filtered_f)))

filtered_img = cv2.normalize(filtered_img, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow('Original Image', img)
cv2.imshow('Ideal Lowpass Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
