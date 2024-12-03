
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# API-Endpunkt zum Abrufen von Materialien
@app.route('/api/materials', methods=['GET'])
def get_materials():
    conn = sqlite3.connect('/app/db/materials.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Material, Kategorie FROM materials")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/', methods=['GET'])
def home():
    return "Flask API läuft! Besuche /api/materials, um die Daten zu sehen."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
