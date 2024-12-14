# Import necessary modules
# Flask: Framework for building the web application
# jsonify: Converts Python objects to JSON format for API responses
# sqlite3: Module to interact with SQLite databases
from flask import Flask, jsonify
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Define an API endpoint to retrieve materials
@app.route('/api/materials', methods=['GET'])
def get_materials():
    """
    Fetches materials and their categories from the database.

    Steps:
    1. Connect to the SQLite database located at '/app/db/materials.db'.
    2. Execute a SQL query to fetch the 'Material' and 'Kategorie' columns from the 'materials' table.
    3. Retrieve the results and close the database connection.
    4. Return the results as a JSON response.

    Returns:
        JSON: A list of materials with their categories.
    """
    # Connect to the database
    conn = sqlite3.connect('/app/db/materials.db')
    cursor = conn.cursor()

    # Execute SQL query to fetch materials and their categories
    cursor.execute("SELECT Material, Kategorie FROM materials")

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return the data as a JSON response
    return jsonify(rows)

# Define the home route
@app.route('/', methods=['GET'])
def home():
    """
    Displays a basic message indicating the API is running.

    Returns:
        str: A message confirming that the Flask API is operational.
    """
    return "Flask API is running! Visit /api/materials to view the data."

# Run the Flask application
if __name__ == "__main__":
    """
    Starts the Flask application on host 0.0.0.0 (accessible externally)
    and port 5000 in debug mode (for development purposes).
    """
    app.run(host='0.0.0.0', port=5000, debug=True)

