import pymupdf

from data_model.document import Document

class ReadPDFStep:
    def __init__(self):
        self.name: str = "read_pdf"

    def run(self, doc:Document):
        pdf = pymupdf.open(doc.path)

        for page in pdf:
            doc.ocr_pages.append(page)

        text = " ".join(page.get_text() for page in pdf)

        doc.ocr_text = text

        return doc
