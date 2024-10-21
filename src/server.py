from flask import Flask, jsonify
from src.inventory import Inventory

app = Flask(__name__)

inventory = Inventory('inventory.csv')

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(inventory.items)

if __name__ == '__main__':
    app.run(debug=True)
