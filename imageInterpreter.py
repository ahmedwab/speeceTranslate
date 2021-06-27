import cv2
import pytesseract as pt



def getTextFromImage (filename):
    try:
        image = cv2.imread(filename)
        text = pt.image_to_string(image)
        print(text)
        return text
    except:
        print("Something went wrong")

