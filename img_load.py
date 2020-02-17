import cv2
image = cv2.imread("./image.jpg")
cv2.imshow("Dog & cat", image)
cv2.waitKey(0)
cv2.destroyAllWindows()