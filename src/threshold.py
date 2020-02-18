import cv2 as cv

image = cv.imread("../images/image.jpg")
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, threshold_image = cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)
cv.imshow("Dog & cat wb", threshold_image)
cv.waitKey(0)
cv.destroyAllWindows()