import cv2
import pytesseract
import os

path = os.path.join('.', 'textImage.jpeg')

image = cv2.imread(path)

if image is None:
    print("Error: Image not found. Check the path.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(thresh)

print("\nDetected Text:\n")
print(text)

with open("detected_text.txt", "w") as file:
    file.write(text)

print("\nText saved to detected_text.txt")

data = pytesseract.image_to_data(thresh)

for line in data.splitlines()[1:]:
    parts = line.split()

    if len(parts) == 12:
        x = int(parts[6])
        y = int(parts[7])
        w = int(parts[8])
        h = int(parts[9])

        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)

# Show results
cv2.imshow("Original Image", image)
cv2.imshow("Processed Image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()