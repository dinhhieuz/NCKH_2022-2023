import cv2 

image = cv2.imread('tuluan1.jpg')
W, H, C = image.shape

image = image[50:int(H/3), :int(W/3)]
cv2.imshow("image", image)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow("gray", gray)
edged = cv2.Canny(gray, 100, 200)
cv2.imshow("edged", edged)
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1=image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3)
cv2.imshow("contours",image1)

cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
image2 = image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)
cv2.imshow("Top 1 contours",image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
