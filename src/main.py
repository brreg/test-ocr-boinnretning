from protocol.step_protocol import PipelineStep
from pipeline.pipeline import Pipeline
from data_model.bankruptcy import BankruptcyDocument
from step.ReadPDFStep import ReadPDFStep
from step.CleanTextStep import CleanTextStep

from pathlib import Path


if __name__ == "__main__":
    pipe = Pipeline(steps=[
        ReadPDFStep(),
        CleanTextStep()
    ])

    BASE_DIR = Path(__file__).parent

    for filepath in ["testdata/pdf/Veileder_reelle_rettighetshavere_bokmaal (3).pdf"]:
        doc = BankruptcyDocument(id="test", path=Path(BASE_DIR / filepath))
        out = pipe.run(doc)
        print(out.ocr_text[:1000])
    #print(out.org_nr)
    #print(meta)

    # save document as JSON?
