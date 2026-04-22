from data_model.document import Document

class CleanTextStep:
    name= "clean_text"

    def run(self, doc: Document):
        text = doc.ocr_text

        if text is None:
            return doc

        # fjern tabs
        text = text.replace("\t", " ")
        
        # fjern ny linje
        text = text.replace("\n", " ")

        doc.ocr_text = text
        return doc

