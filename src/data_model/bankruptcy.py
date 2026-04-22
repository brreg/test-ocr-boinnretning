from data_model.document import Document
from typing import Optional
from dataclasses import dataclass, field

@dataclass
class BankruptcyDocument(Document):

    # Uttrekk flyttet til subclass
    org_nr: Optional[str] = None
    punishable_circumstances: Optional[bool] = None