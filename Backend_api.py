
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import sqlite3
import os
import requests

app = Flask(__name__)
CORS(app)

# Connect to the SQLite database

DATABASE = requests.get('https://github.com/AmrinderG/test-ag03/raw/refs/heads/main/project_database.db')


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# API Route to Fetch All Master Tags
@app.route('/master-tag-list', methods=['GET'])
def get_all_tags():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Central_Equipment")
    rows = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in rows])

# API Route to Search Master Tags
@app.route('/master-tag-list/search', methods=['GET'])
def search_tags():
    query = request.args.get('q', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Central_Equipment WHERE Tag_No LIKE ? OR Instrument_Type LIKE ?", (f"%{query}%", f"%{query}%"))
    rows = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in rows])

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import sqlite3
import os 

app = Flask(__name__)
CORS(app)

# Connect to the SQLite database
DATABASE = requests.get('https://github.com/AmrinderG/test-ag03/raw/refs/heads/main/project_database.db')


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# API Route to Fetch All Master Tags
@app.route('/master-tag-list', methods=['GET'])
def get_all_tags():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Central_Equipment")
    rows = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in rows])

# API Route to Search Master Tags
@app.route('/master-tag-list/search', methods=['GET'])
def search_tags():
    query = request.args.get('q', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Central_Equipment WHERE Tag_No LIKE ? OR Instrument_Type LIKE ?", (f"%{query}%", f"%{query}%"))
    rows = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)

