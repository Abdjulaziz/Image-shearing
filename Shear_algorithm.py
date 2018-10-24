import cv2
import numpy as np

#Basic image read
img = cv2.imread("2.PNG", 0)
Bx = 1
By = 1
rows = img.shape[0]
cols = img.shape[1]

#Image copies
CopyOf_img1 = np.zeros((rows+600,cols,3), np.uint8)
CopyOf_img2 = np.zeros((rows+600,cols,3), np.uint8)
CopyOf_img3 = np.zeros((rows,cols+600,3), np.uint8)
CopyOf_img4 = np.zeros((rows,cols+600,3), np.uint8)

#ShearY algorithm
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        n = Bx * j
        k = img[i, j]
        CopyOf_img1[i + n, j] = k

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        n = By * j
        k = img[i, j]
        CopyOf_img2[i - n + img.shape[1], j] = k




#ShearX algorithm
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        n = Bx * i
        k = img[i, j]
        CopyOf_img3[i, j + n] = k

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        n = By * i
        k = img[i, j]
        CopyOf_img4[i, j - n + img.shape[0]] = k



#Default image
cv2.imshow("defult",img)

#ShearX
cv2.imshow("shearY1",CopyOf_img1)
cv2.imshow("shearY2",CopyOf_img2)

#ShearY
cv2.imshow("shearX1",CopyOf_img3)
cv2.imshow("shearX2",CopyOf_img4)

#Write images
cv2.imwrite('shearY1.PNG', CopyOf_img1)
cv2.imwrite('shearY2.PNG', CopyOf_img2)
cv2.imwrite('shearX1.PNG', CopyOf_img3)
cv2.imwrite('shearX2.PNG', CopyOf_img4)


#Any key can be pressed to destroy the image
cv2.waitKey(0)
cv2.destroyAllWindows()