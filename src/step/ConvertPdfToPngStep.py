import pymupdf
from data_model.document import Document

class ConvertPdfToPngStep:
    def __init__(self):
        self.name: str = "convert_pdf_to_png"

    def run(self, doc:Document):
        pdf = pymupdf.open(doc.path)

        for page_num in range(len(pdf)):
            page = pdf[page_num]
            pix = page.get_pixmap()
            doc.img_pages.append(pix)
            
            #pix.save(f"page_{page_num+1}.png")

        return doc
