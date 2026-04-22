# OCR for boinnretninger

## Oppbygning
Koden er basert rundt klassene Pipeline (se src/pipeline/pipeline.py) og Document (se src/data_model/document.py). En pipeline tar en et liste med objekter av protokollen PipelineStep (se src/protocol/ste_protocol.py) og et Document-objekt som prosesseres av hvert PipelineStep. 

## OCR
Hvis man ønsker et OCR-steg trenger kan pytesseract benyttes. Pytesseract er en wrapper for Tessaract som ikke er en python-pakke. For å bruke Tessaract lag et Docker image og kjør som container. 

## Image og container
For å kjøre pipeline, bygg image:

```podman build -t pipeline-test .```
(punktum indikerer at image skal bygge fra denne mappen)


For å kjøre containeren uten internett (teste ingen tilgang) legg til --network=none:
```podman run --rm --network=none pipeline-test```