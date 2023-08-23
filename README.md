# Optical Character Recognition (OCR)

This code demonstrates how to use the pytesseract library and the PIL library in Python to perform optical character recognition (OCR) on an image.

## Prerequisites

- Python 3.x
- pytesseract library
- PIL library

## Installation

1. Install pytesseract library using `pip`:
   ```
   pip install pytesseract
   ```

2. Install PIL library using `pip`:
   ```
   pip install Pillow
   ```

## Usage

1. Replace `'path/to/your/image.jpg'` with the actual path to your image file.

2. Run the code and it will perform OCR on the image and extract the text.

3. The extracted text will be displayed in the console.

## Example

```python
import pytesseract
from PIL import Image

image_path = 'path/to/your/image.jpg'

image = Image.open(image_path)

text = pytesseract.image_to_string(image, lang='eng')

print(text)
```

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).
