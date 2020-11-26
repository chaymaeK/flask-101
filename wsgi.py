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


@app.route(f'{BASE_URL}/products', methods=['POST'])
def create_one_product():
    data = request.get_json()

    if data is None:
        abort(400)

    name = data.get('name')

    if name is None:
        abort(400)

    if name == '' or not isinstance(name, str):
        abort(422)

    next_id = next(IDENTIFIER_GENERATOR)
    new_product = {'id' : next_id , 'name' : name }
    PRODUCTS[next_id] = new_product #{'id' : next_id , 'name' : name }

    return jsonify(new_product), 201 #PRODUCTS[next_id]), 201


@app.route(f'{BASE_URL}/products/<int:product_id>', methods=['PATCH'])
def update_one_product(product_id):
    data = request.get_json()
    if data is None:
        abort(400)

    name = data.get('name')

    if name is None:
        abort(400)

    if name == '' or not isinstance(name, str):
        abort(422)

    product = PRODUCTS.get(product_id)

    if product is None:
        abort(404)

    PRODUCTS[product_id]['name'] = name

    return None, 204
