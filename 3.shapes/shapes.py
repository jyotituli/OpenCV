import numpy as np
import cv2

#img = cv2.imread('lena.jpg',0)

img = np.zeros([512, 512, 3], np.uint8)
img = cv2.line(img,  (0, 0), (255, 255), (255, 0, 0), 7)
img = cv2.arrowedLine(img,  (0, 255), (255, 255), (255, 0, 0), 7)

#for rectangle
#x1,y1 - - - - -
#|
#|
#|
#|- - - - -- - -x2,y2
img = cv2.rectangle(img, (384,0), (510,255), (0,0,255), 5)

#circle
img = cv2.circle(img, (447, 63), 64, (0, 255, 0), -1)

#putText
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Open CV',(10, 500), font, 4, (255,255,255), 10, cv2.LINE_AA)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()