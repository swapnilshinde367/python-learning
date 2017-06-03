# pylint: skip-file
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread( 'test_img.png', cv2.IMREAD_COLOR )

# image obj, position, size, color, width
cv2.line( img, ( 0,0 ), ( 150, 150 ), ( 255, 0, 0 ), 2 )
cv2.rectangle( img, ( 50, 250 ), ( 150, 150 ), ( 0, 255, 0 ), 2 )
cv2.circle( img, ( 175, 250 ), 35, ( 0, 0, 255 ), -5 )
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText( img, 'Test', ( 130, 190 ), font, 1, ( 155, 150, 90 ), 2, cv2.LINE_AA )

# Add Color to certain area of image
# img[ 55, 55 ] = [ 255, 255, 255 ]
# px = img[ 55, 55 ]
img[ 10:75, 10:75 ] = [ 255, 255, 255 ]

# Copy image using pixel start and end points
roi_image_cropped = img[ 130:220, 130:220 ]
img[ 50:140, 50:140 ] = roi_image_cropped

cv2.imshow( 'image', img )
cv2.waitKey()
cv2.destroyAllWindows()