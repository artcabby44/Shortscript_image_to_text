import pytesseract as tess
from PIL import Image

#tesseract_directory
tess.pytesseract.tesseract_cmd = r'C:\Users\trojanware\AppData\Local\Tesseract-OCR\tesseract.exe'

#img to string
img = Image.open('it.jpg')
strg = tess.image_to_string(img)
print(strg)
