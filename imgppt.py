import cv2 as cv

# binary image
# img=cv.imread("binary.jpg", 0)

# cv.imshow("binary", img)
# print(type(img))
# print(img.shape)
# print(img.dtype)
# print(img.size)
#print(img)



# grayscale image
# img=cv.imread(r"C:/Users/HP/Pictures/Saved Pictures/Shanks - Red Hair - Red-Haired Shanks.jpg", 0)

# cv.imshow("gray", img)
# print(type(img))
# print(img.shape)
# print(img.dtype)
# print(img.size)
# print(img)


# color image
img=cv.imread(r"C:/Users/HP/Pictures/Saved Pictures/Shanks - Red Hair - Red-Haired Shanks.jpg")

cv.imshow("color", img)
print(type(img))
print(img.shape)
print(img.dtype)
print(img.size)
print(img)


cv.waitKey(0)
cv.destroyAllWindows()

