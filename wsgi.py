# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, abort, jsonify

app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'test'}
}


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods=['GET'])
def read_many_products():
    products = tuple(PRODUCTS.values())
    return jsonify(products), 200

@app.route('/api/v1/products/<int:id>', methods=['GET'])
def read_one_product(id):
    product = PRODUCTS.get(id)
    if product is None:
        abort(404)

    return jsonify(product), 200

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def delete_one_product(id):
    product = PRODUCTS.pop(id, None)
    if product is None:
        abort(404)

    return '', 202

