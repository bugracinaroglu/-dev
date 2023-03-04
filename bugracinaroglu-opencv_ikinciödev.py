import cv2 as cv
import numpy as np 

class red:
    def mask(self):
        self.blured=cv.blur(self.frame,(20,20))
        self.img_hsv=cv.cvtColor(self.blured, cv.COLOR_BGR2HSV)
        self.lower_red = np.array([140,80,50]) 
        self.upper_red = np.array([180,255,255]) 
        mask = cv.inRange(self.img_hsv, self.lower_red, self.upper_red)
        self.img_result = cv.bitwise_and(self.frame, self.frame, mask=mask)
        cv.imshow("dfds",self.img_result)
    def contour(self):
        self.canny=cv.Canny(self.img_result,125,175)
        self.contours, self.hierarchies=cv.findContours(self.canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
        for contour in self.contours:
            (x,y), radius = cv.minEnclosingCircle(contour)
            self.center = (int(x),int(y))
            radius =int(radius)
            cv.circle(self.frame,self.center,4,(0,0,0),-1)
            cv.drawContours(self.frame,contour,-1,(255,0,0),5)
                     
    def distance(self):
        y=int(self.frame.shape[0]/2)
        x=int(self.frame.shape[1]/2)
        distance=float(((x-self.center[0])**2+(y-self.center[1])**2)**(1/2))
        distance=round(distance,3)
        cv.putText(self.frame,f"Distance={distance}",(15,25),cv.FONT_HERSHEY_TRIPLEX,0.6,(0,0,0),1,cv.LINE_AA)
        cv.line(self.frame,self.center,(x,y),(0,25,25),thickness=3)

    def start(self):
        self.capture=cv.VideoCapture("reddetection.mp4")
        while True:
            isTrue, self.frame=self.capture.read()
            self.mask()
            self.contour()
            self.distance()
            cv.imshow("video",self.frame)
            if cv.waitKey(20) & 0xFF==ord("d"):
                break

deneme=red()
deneme.start()
