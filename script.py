import flask
import sqlite3
from flask import request, jsonify

"""
- The product database has 3 tables FRUITS, CERIALS AND VEGETABLES
- Our API allows users to filter by three fields: fruits, cerials, vegetables
"""

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Products API</h1><p>An API to show demands for products according to number mentions.</p>'''

@app.route('/api/products/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('products.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_fruits = cur.execute('SELECT * FROM fruits;').fetchall()
    all_cerials = cur.execute('SELECT * FROM cerials;').fetchall()
    all_vegetables = cur.execute('SELECT * FROM vegetables;').fetchall()

    return jsonify(all_fruits, all_cerials, all_vegetables)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/products=fruits', methods=['GET'])
def api_fruits():
    conn = sqlite3.connect('products.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_fruits = cur.execute('SELECT * FROM fruits;').fetchall()

    return jsonify(all_fruits)

@app.route('/api/products=cerials', methods=['GET'])
def api_cerials():
    conn = sqlite3.connect('products.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_cerials = cur.execute('SELECT * FROM cerials;').fetchall()

    return jsonify(all_cerials)

@app.route('/api/products=vegetables', methods=['GET'])
def api_vegetables():
    conn = sqlite3.connect('products.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_vegetables = cur.execute('SELECT * FROM vegetables;').fetchall()

    return jsonify(all_vegetables)

if __name__ == '__main__':
    app.run()

"""
    API Endpoints
    http://127.0.0.1:5000/api/products/all
    http://127.0.0.1:5000/api/products=fruits
    http://127.0.0.1:5000/api/products=cerials
    http://127.0.0.1:5000/api/products=vegetables
"""
