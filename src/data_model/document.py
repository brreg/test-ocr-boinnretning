from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Any, Optional
from pymupdf import Pixmap

@dataclass
class Document:
    id: str 
    path: Path 

    # OCR
    img_pages: List[Pixmap] = field(default_factory=list)
    ocr_pages: List[str] = field(default_factory=list)
    ocr_text: Optional[str] = None

    # metadata (e.g. models, date processed)
    meta: Dict[str, Any] = field(default_factory=dict)

    def text(self) -> str:
        return self.ocr_text or ""