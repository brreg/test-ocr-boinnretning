FROM fedora:latest

# Installer Tesseract + Python 
RUN dnf install -y \
    tesseract \
    python3 \
    python3-pip

WORKDIR /app
COPY . /app

RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

CMD ["python3", "src/main.py"]