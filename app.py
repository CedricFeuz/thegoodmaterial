# Import necessary modules
# Flask: Framework for building the web application
# render_template: Renders HTML templates
# jsonify: Converts Python data to JSON format for API responses
# pandas: Used for loading and processing CSV files
from flask import Flask, render_template, jsonify
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Load the CSV file into a DataFrame
# 'materials.csv' contains material data to be displayed in the frontend
materials_df = pd.read_csv('materials.csv')

# Define the route for the homepage
@app.route('/')
def home():
    """
    Displays the homepage of the application.
    
    Returns:
        HTML template (index.html): The rendered homepage.
    """
    return render_template('index.html')

# Define the API endpoint to retrieve material data
@app.route('/materials')
def get_materials():
    """
    API endpoint: Provides material data as JSON.
    
    Steps:
        1. Convert the DataFrame into a list of dictionaries (JSON-compatible).
        2. Send the data to the client.
    
    Returns:
        JSON object: Material data from the CSV file.
    """
    # Convert the DataFrame to a JSON-compatible structure
    materials = materials_df.to_dict(orient='records')
    return jsonify(materials)

# Run the Flask application
if __name__ == '__main__':
    """
    Starts the Flask server in debug mode and binds it to all available IP addresses (0.0.0.0).
    Debug mode allows for easier troubleshooting and automatic server restarts when code changes.
    """
    app.run(debug=True, host='0.0.0.0')

