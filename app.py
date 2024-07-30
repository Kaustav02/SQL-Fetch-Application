from flask import Flask, request, jsonify
import os
from utils.db_utils import execute_sql_command
from utils.file_utils import read_sql_from_xml

app = Flask(__name__)

@app.route('/query/<filename>', methods=['GET'])
def query_db(filename):
    sql_file_path = os.path.join('D:/SQL Fetch/', filename)  # Dynamically set the file path

    # Read SQL command from XML file
    sql_command = read_sql_from_xml(sql_file_path)

    # Replace placeholders in the SQL command with URL parameters
    for key, value in request.args.items():
        placeholder = f"[params.{key}]"
        sql_command = sql_command.replace(placeholder, value)

    result = execute_sql_command('db/test.db', sql_command)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
