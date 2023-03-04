import cv2 as cv


name="photo/dog.jpg"
img=cv.imread(name, -1)
img=cv.resize(img,(800,800),interpolation=cv.INTER_CUBIC)
img1=cv.imread(name, -1)
img1=cv.resize(img1,(800,800))

def click_event(event, x, y, flags, param):
    global img
    global img1
    global save
    global action
    if event==cv.EVENT_LBUTTONDOWN and not(flags & cv.EVENT_FLAG_CTRLKEY) and not(flags &cv.EVENT_FLAG_ALTKEY):
        img1=cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
        cv.imshow("image", img1)
        img=img1.copy()

    if event==cv.EVENT_RBUTTONDOWN and not(flags & cv.EVENT_FLAG_CTRLKEY) and not(flags &cv.EVENT_FLAG_ALTKEY):
        img1=cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
        cv.imshow("image", img1)
        img=img1.copy()
    
    if event ==cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_CTRLKEY):
        if action=="rectangle":
            if len(points)==0:
                pass
            else:
                point=(x,y)
                points.append(point)
                cv.rectangle(img1, points[-1], points[-2], [255, 255, 255], 15)
                cv.imshow("image", img1)
                img1=img.copy()
        if action=="circle":
            if len(points)==0:
                pass
            else:
                radius=int(((points[-1][0]-points[0][0])**2+(points[-1][1]-points[0][1])**2)**0.5)
                point=(x,y)
                points.append(point)
                cv.circle(img1,points[0],radius,(255,255,255),5)
                cv.imshow("image", img1)
                img1=img.copy()
    if event == cv.EVENT_LBUTTONDOWN and (flags & cv.EVENT_FLAG_CTRLKEY):
        action = "rectangle"
        points.clear()
        points.append((x,y))

    #dikdörtgeni çizmek
    if event ==cv.EVENT_LBUTTONUP and (flags & cv.EVENT_FLAG_CTRLKEY):
        action=""
        save=img[min(points[-1][1],points[0][1]):max(points[-1][1],points[0][1]),min(points[-1][0],points[0][0]):max(points[-1][0],points[0][0])]
        cv.rectangle(img, points[-1], points[0], [255, 255, 255], 5)
        cv.imwrite("crop.jpg", save)
        crop=cv.imread("crop.jpg")
        cv.imshow("cropped",crop)
        cv.imshow("image", img)

    #texti yazdırmak    
    if event == cv.EVENT_LBUTTONDOWN and (flags & cv.EVENT_FLAG_ALTKEY):
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        color=(int(blue),int(green),int(red))
        font = cv.FONT_HERSHEY_COMPLEX
        cv.putText(img, "ZOR BAYA", (x, y), font, 0.5, color, 1)
        cv.imshow("image", img)


    if event == cv.EVENT_RBUTTONDOWN and (flags & cv.EVENT_FLAG_CTRLKEY):
        action="circle"
        points.clear()
        points.append((x, y))
    
    #çemberi çizmek
    if event ==cv.EVENT_RBUTTONUP and (flags & cv.EVENT_FLAG_CTRLKEY):
        action=""
        radius = int(((points[-1][0] - points[0][0]) ** 2 + (points[-1][1] - points[0][1]) ** 2) ** 0.5)
        cv.circle(img, points[0], radius, (255, 255, 255), 5)
        cv.imshow("image", img)
    
    #en son hali
    if event == cv.EVENT_RBUTTONDOWN and (flags & cv.EVENT_FLAG_ALTKEY):
        cv.imwrite("result.jpg", img)
        result=cv.imread("result.jpg")
        cv.imshow("result",result)

action="rectangle"
cv.imshow("image",img)
points=[]
cv.setMouseCallback("image",click_event)
cv.waitKey(0)
cv.destroyAllWindows()
