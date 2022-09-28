import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/cat.png')
kernelVal = -1;
while not (kernelVal > 0 and kernelVal < 11) or ValueError:
    try:
        kernelVal = int(input("Input a number between 1-10 (1 = less smoothing, 10 = more smoothing)\n"))
        if kernelVal < 1 or kernelVal > 10:
            print("Value out of range.")
        else:
            break
    except ValueError:
        print("Value must be an integer.")

kernel = np.ones((kernelVal, kernelVal), np.float32)/np.square(kernelVal)
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Smoothed (filter matrix : ' + str(kernelVal)+'x'+str(kernelVal)+')')
plt.xticks([]), plt.yticks([])
plt.show()
