import cv2
import pytesseract
import os

path =  os.path.join('.','textImage.jpeg')
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Detect text
text = pytesseract.image_to_string(thresh)

print("Detected Text:")
print(text)
with open("output.txt", "w") as file:
    file.write(text)
# Show image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()