# pylint: skip-file
import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc( *'XVID' )
out = cv2.VideoWriter( 'video_output.avi', fourcc, 20.0, ( 480,640 ) )

while True:
	ret, frame = cap.read()
	out.write( frame )
	cv2.imshow( 'frame', frame )
	if cv2.waitKey(1) & 0xFF == ord( 'q' ):
		break
cap.release()
out.release()
cv2.destroyAllWindows()