from data_model.document import Document
class FindOrgNrStep:

    def __init__(self):
        self.name = "find_orgnr_step"
        self.model = None

    def run(self, doc: Document) -> Document:
        for page in doc.ocr_pages:
            # noe slikt som
            if "organisasjonsnummer" in page:
                pass
                # bruk modellen på en eller annen måte for å finne org nr. 

        # Alternativ kjør alle sider gjennom modell? 

        # ideer?? : 
        # NER modell fra Spacy med nlp.to_disk? 
        # noen små modeller fra hugging face lokalt? nb-bert-base-ner?

        # ideer til entiteter: 
        # Prim_orgnr
        # Other_orgnr - for andre organisasjonsnumre som nevnes i dokumentet.

        # Uansett så er dette modeller som må trenes


        return doc