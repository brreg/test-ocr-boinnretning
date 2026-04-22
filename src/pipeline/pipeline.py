from dataclasses import dataclass
from typing import Dict, List, Any, Protocol

from data_model.document import Document
from protocol.step_protocol import PipelineStep

@dataclass
class Pipeline:
    steps: List[PipelineStep]

    def run(self, doc:Document ) -> Document:
        for step in self.steps:
            doc = step.run(doc)
        return doc