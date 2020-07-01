from PIL import Image, ImageEnhance
import pytesseract
import docx
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

#sets image path, opens image
path = input("Paste image path: ")
img = Image.open(path)
#converts image text to string format
text = pytesseract.image_to_string(img)
#writes to word doc
img_doc = docx.Document()
img_doc.add_paragraph(text)
img_doc.save("E:/img_to_word.docx")

print("Your document is ready!")
