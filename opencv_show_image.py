# pylint: skip-file
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread( 'test_img.png', cv2.IMREAD_GRAYSCALE )

cv2.imshow( 'image', img )
cv2.waitKey()
cv2.destroyAllWindows()