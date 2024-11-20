from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# CSV-Datei laden
materials_df = pd.read_csv('materials.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/materials')
def get_materials():
    # Konvertiere DataFrame in JSON
    materials = materials_df.to_dict(orient='records')
    return jsonify(materials)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
