import cv2 as cv
import numpy as np
a = 20
x0=y0=50
img = np.zeros((20*a,20*a,3),np.uint8)

for i in range(6):
    img = cv.circle(img,(x0+7*a,y0+15*a-2*i*a),a,(255,255,255),1)
longrad = 75
shortrad = 40
img=cv.ellipse(img,(x0+3*a,y0+7*a),(longrad,shortrad),45,0,360,(205,206,120),-1)
img=cv.ellipse(img,(x0+3*a,y0+13*a),(longrad,shortrad),-45,0,360,(125,255,10),-1)
img=cv.ellipse(img,(x0+11*a,y0+7*a),(longrad,shortrad),-45,0,360,(100,200,50),-1)
img=cv.ellipse(img,(x0+11*a,y0+13*a),(longrad,shortrad),45,0,360,(125,50,36),-1)

img=cv.rectangle(img,(x0+6*a,y0+2*a),(x0+8*a,y0+4*a),(0,200,200),5)

img=cv.ellipse(img,(x0,y0+2*a),(125,shortrad),0,0,-90,(100,0,250),6)
img=cv.ellipse(img,(x0+14*a,y0+2*a),(125,shortrad),0,180,270,(100,0,250),6)

img=cv.circle(img,(x0,y0),8,(100,0,250),-1)
img=cv.circle(img,(x0+14*a,y0),8,(100,0,250),-1)

cv.imshow("image",img)
cv.waitKey(0)
