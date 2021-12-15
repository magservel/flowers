from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS

from src.interface import Interface

app = Flask(__name__)
CORS(app)

interface = Interface()


@app.route("/api/train")
def train():
    response = interface.on_train()
    return jsonify(response)


@app.route("/api/add", methods=['OPTIONS', 'POST'])
def add():
    data = request.get_json(force=True)
    x = data.get("add_x")
    y = data.get("add_y")
    use = data.get("data_use")
    response = interface.on_add(x=x, y=y, use=use)
    return jsonify(response)


@app.route("/api/list")
def list():
    response = interface.on_list()
    return jsonify(response)


@app.route("/api/infer", methods=['OPTIONS', 'POST'])
def infer():
    data = request.get_json(force=True)
    x = data.get("infer_x")
    response = interface.on_infer(x=x)
    return jsonify(response)


if __name__ == '__main__':
    pass

