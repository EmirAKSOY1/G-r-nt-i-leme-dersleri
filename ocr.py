"""
OCR UYGULAMA

OCR:Optical Character Recognition(Optik Karakter Tanıma)

Kayna:https://medium.com/@ibrahimirdem/tesseract-ile-yaz%C4%B1-karakteri-tan%C4%B1ma-python-8ca5e746951

64-Bit İndirme Linki
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.0.0-beta.4.20180912.exe
"""


import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'
a=pytesseract.image_to_string(Image.open('resim/captcha.png'), lang='tur')

print(a)