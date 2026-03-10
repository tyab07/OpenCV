import cv2
import easyocr
import os

# Initialize OCR reader
reader = easyocr.Reader(['en'])

# Image path
path = os.path.join('.', '09_text_detection', 'textImage.jpeg')

# Read image
image = cv2.imread(path)

if image is None:
    print("Image not found. Check path.")
    exit()

# Detect text
results = reader.readtext(image)

detected_text = ""

# Loop through detected text
for (bbox, text, confidence) in results:

    detected_text += text + "\n"

    # Get box coordinates
    (top_left, top_right, bottom_right, bottom_left) = bbox

    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))

    # Draw rectangle
    cv2.rectangle(image, top_left, bottom_right, (0,255,0), 2)

    # Put detected text
    cv2.putText(image, text, top_left,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0,255,0), 2)

# Print detected text
print("\nDetected Text:\n")
print(detected_text)

# Save detected text
with open("detected_text.txt","w") as file:
    file.write(detected_text)

print("Text saved to detected_text.txt")

# Show result
cv2.imshow("Text Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()