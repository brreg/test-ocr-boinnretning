import pytesseract 
from PIL import Image 
from data_model.document import Document

class TesseractOCRStep:
    def __init__(self):
        self.name: str = "tesseract_OCR_step"

    def run(self, doc: Document) -> Document:
        for page in doc.img_pages:
            img = Image.open(page) # funker dette når det ikke er en path, men object?
            text = pytesseract.image_to_string(img) 
            
            # lagre text resultatet
            doc.ocr_pages.append(text)
            if doc.text() == "":
                doc.text = text
            else:
                doc.ocr_text = doc.ocr_text + " " + text
        
        return doc