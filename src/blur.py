import cv2 as cv

image = cv.imread("../images/guys.jpg")
blur = cv.GaussianBlur(image, (63, 63), cv.BORDER_DEFAULT)

cv.imshow("Russian gopniks", blur)
cv.waitKey(0)
cv.destroyAllWindows()