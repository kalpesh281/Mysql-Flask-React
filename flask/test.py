from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # This enables cross-origin requests, allowing React to access the Flask API

# MySQL Configuration from environment variables
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)

# Helper function to convert bytes to string if needed
def convert_bytes(data):
    if isinstance(data, bytes):
        return data.decode('utf-8', errors='ignore')  # Decoding bytes to string (you can handle errors as needed)
    return data

# Route to fetch column names and data from all tables
@app.route('/api/tables', methods=['GET'])
def get_tables_columns_data():
    table_data = {}

    try:
        # Get all tables in the database
        cur = mysql.connection.cursor()
        cur.execute("SHOW TABLES")
        tables = cur.fetchall()

        # For each table, fetch column names and the first 10 rows
        for table in tables:
            table_name = table[f"Tables_in_{os.getenv('MYSQL_DB')}"]  # Get table name from the result
            cur.execute(f"DESCRIBE {table_name}")
            columns = cur.fetchall()

            # Extract column names
            column_names = [column['Field'] for column in columns]

            # Fetch first 10 rows of data for the table
            cur.execute(f"SELECT * FROM {table_name} LIMIT 10")
            data = cur.fetchall()

            # Convert any bytes data to string
            data = [{key: convert_bytes(value) for key, value in row.items()} for row in data]

            # Add table, column names, and data to the dictionary
            table_data[table_name] = {
                "columns": column_names,
                "data": data
            }
        
        cur.close()

        # Return both column names and data for each table as a JSON response
        return jsonify(table_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to fetch data for the selected column from a specific table
@app.route('/api/column_data', methods=['GET'])
def get_column_data():
    table_name = request.args.get('table')
    column_name = request.args.get('column')

    if not table_name or not column_name:
        return jsonify({"error": "Table and column are required"}), 400

    try:
        # Get data for the selected column from the table
        cur = mysql.connection.cursor()
        query = f"SELECT {column_name} FROM {table_name} LIMIT 10"
        cur.execute(query)
        data = cur.fetchall()

        # Convert any bytes data to string
        data = [convert_bytes(row[column_name]) for row in data]

        cur.close()

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
