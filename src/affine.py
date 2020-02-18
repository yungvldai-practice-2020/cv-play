import numpy as np
import cv2 as cv

image = cv.imread('../images/tower.jpg')
rows, cols, ch = image.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv.getAffineTransform(pts1, pts2)
affine = cv.warpAffine(image, M, (cols, rows))
cv.imshow("Tower", affine)
cv.waitKey(0)
cv.destroyAllWindows()