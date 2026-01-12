import cv2 as cv

# Read the image
img=cv.imread("C:/Users/HP/Pictures/Saved Pictures/Shanks - Red Hair - Red-Haired Shanks.jpg") # 0 for grayscale and 1 for color. if  not specified, it will be read as color image 

# Display the image
# cv.imshow("image",img)
 
# Wait for a key press
cv.waitKey(0)

# Destroy all windows
cv.destroyAllWindows()

# Save the image
# cv.imwrite("RED HAIRED SHANKS.jpg",img)

# Print the shape of the image
print(img.shape)

# Print the type of the image
print(type(img))

# Print the size of the image
print(img.size)

# convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray",gray)

cv.waitKey(0)

cv.destroyAllWindows()
