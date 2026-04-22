from typing import Protocol

from data_model.document import Document


class PipelineStep(Protocol):
    name: str

    # Lag en signatur for metoden run
    def run(self, doc: Document) -> Document: ...