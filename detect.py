import cv2 as cv

face_cascade = cv.CascadeClassifier('./haarcascade_frontalface_default.xml')
image = cv.imread('face.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

cv.imshow('Detect', image)
cv.waitKey(0)
cv.destroyAllWindows()