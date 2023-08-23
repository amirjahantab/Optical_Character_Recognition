import pytesseract
from PIL import Image

image_path = 'path/to/your/image.jpg'

image = Image.open(image_path)

text = pytesseract.image_to_string(image, lang='eng')

print(text)
