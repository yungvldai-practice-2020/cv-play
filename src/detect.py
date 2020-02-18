import cv2 as cv

face_cascade = cv.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('../haarcascades/haarcascade_eye.xml')
image = cv.imread('../images/face.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
cv.imshow('Detect', image)
cv.waitKey(0)
cv.destroyAllWindows()
