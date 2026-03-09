import cv2
import os

# Use full or relative path to your image
path = os.path.join(os.path.dirname(__file__), 'birds.jpeg')

# Load image safely
img = cv2.imread(path)
if img is None:
    raise FileNotFoundError(f"Image not found at path: {path}")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, invert = cv2.threshold(img_gray, 70, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, hierarchy = cv2.findContours(invert, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a copy of original image
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

# Print total number of objects found
print(f"Total objects detected: {len(contours)}")
for cnt in contours:
    x1,y1,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,23,255),1)
# Show images
cv2.imshow('Original', img_gray)
cv2.imshow('Inverse', invert)
cv2.imshow('Contours', img)

cv2.waitKey(0)
cv2.destroyAllWindows()