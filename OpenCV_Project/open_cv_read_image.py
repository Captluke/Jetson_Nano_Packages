import cv2

print("Library is imported")
img = cv2.imread("/home/jlukas/Desktop/My_Project/Resource/opamp.jpg")

imgrayscale = cv2.imread("/home/jlukas/Desktop/My_Project/Resource/opamp.jpg", cv2.IMREAD_GRAYSCALE)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Org Opamp", img)
cv2.imshow("Gray Opamp", imgGray)
cv2.imshow("Img Grayscale", imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()