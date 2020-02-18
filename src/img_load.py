import cv2 as cv

image = cv.imread("../images/image.jpg")
cv.imshow("Dog & cat", image)
cv.waitKey(0)
cv.destroyAllWindows()