import cv2
import pytesseract

def extract_code_from_image(image_path):
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image)
    return text
