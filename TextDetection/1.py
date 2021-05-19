import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'


# pytesseract.pytesseract.tesseract_cmd
# img = cv2.imread('キャプチャ.png')
img = cv2.imread('111.png')
# img = cv2.imread('222.png')
# img = cv2.imread('abc.png')
# img = cv2.imread('/TextDetection/111.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2Luv)
print(pytesseract.image_to_string(img))
print(pytesseract.image_to_boxes(img))
cv2.imshow('Result', img)
cv2.waitKey(0)