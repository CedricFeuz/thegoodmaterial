# Basis-Image
FROM python:3.9-slim

# Arbeitsverzeichnis
WORKDIR /app

# Anforderungen installieren
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Streamlit-Code kopieren
COPY . .

# Streamlit-App starten
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
