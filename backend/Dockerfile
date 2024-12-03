# Basis-Image
FROM python:3.9-slim

# Arbeitsverzeichnis
WORKDIR /app

# Anforderungen installieren
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Flask-Code kopieren
COPY . .

# Flask-App starten
CMD ["python", "app.py"]
