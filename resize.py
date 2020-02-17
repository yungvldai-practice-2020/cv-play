import cv2 as cv

scale = 0.5
image = cv.imread("./image.jpg")
width = int(image.shape[1] * scale)
height = int(image.shape[0] * scale)
resized = cv.resize(image, (width, height), interpolation=cv.INTER_AREA)
cv.imshow("Dog & cat resized", resized)
cv.waitKey(0)
cv.destroyAllWindows()