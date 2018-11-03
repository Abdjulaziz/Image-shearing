import cv2
import numpy as np

#Image read for the sheared images
img = cv2.imread("shearX1.PNG")
img2 = cv2.imread("shearX2.PNG")
img3 = cv2.imread("shearY1.PNG")
img4 = cv2.imread("shearY2.PNG")
#Shear factor
Bx = -1
By = -1
#sheared images rows and columns
rows = img.shape[0]
cols = img.shape[1]

rows2 = img2.shape[0]
cols2 = img2.shape[1]

rows3 = img3.shape[0]
cols3 = img3.shape[1]

rows4 = img4.shape[0]
cols4 = img4.shape[1]


#Copy of all the images
img_copy = np.zeros((rows,cols,3),np.uint8)

img_copy2 = np.zeros((rows2,cols2,3),np.uint8)

img_copy3 = np.zeros((rows3,cols3,3),np.uint8)

img_copy4 = np.zeros((rows4,cols4,3),np.uint8)

def backwardAlgorithm():
    #Backward mapping of ShearX1
    for i in range(0,rows):
        for j in range(0,cols):
            n  = Bx * i
            k = img[i,j]
            img_copy[i,j + n] = k
    #Backward mapping of ShearX2
    for i in range(0,rows2):
       for j in range(0,cols2):
           n = Bx * i
           k = img2[i, j]
           img_copy2[i, j - n - rows2] = k

    #Bacward mapping for ShearY1
    for i in range(0,rows3):
        for j in range(0,cols3):
            n = By * j
            k = img3[i, j]
            img_copy3[i + n,j] = k

    #Backward mapping for shearY2
    for i in range(0,rows4):
        for j in range(0,cols4):
            n = By * j
            k = img4[i, j]
            img_copy4[i - n - cols4,j] = k



    #Image show and write
    #cv2.imshow("normal",img)
    cv2.imshow("bm",img_copy)

    #cv2.imshow("normal2",img2)
    cv2.imshow("bm22",img_copy2)

    #cv2.imshow("normal3",img3)
    cv2.imshow("bm33",img_copy3)

    #cv2.imshow("normal4",img4)
    cv2.imshow("bm44",img_copy4)

    cv2.imwrite('shearX1Back.PNG', img_copy)
    cv2.imwrite('shearX2Back.PNG', img_copy2)
    cv2.imwrite('shearY1Back.PNG', img_copy3)
    cv2.imwrite('shearY2Back.PNG', img_copy4)

    cv2.waitKey()
    cv2.destroyAllWindows()
backwardAlgorithm()



