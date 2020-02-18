import cv2 as cv

cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('me.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow('frame', frame)
    out.write(frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()