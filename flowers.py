from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS

from src.interface import Interface

app = Flask(__name__)
CORS(app)
api = Api(app)

interface = Interface()


@app.route("/api/start")
def start():
    pass


@app.route("/api/train")
def train():
    print(request.json)
    response = {
        'success': 'OK',
        'message': 'Model trained correctly with accuracy of 95.6%'
    }
    return jsonify(response)


@app.route("/api/add", methods=['OPTIONS', 'POST'])
def add():
    print(request.json)
    response = {
        'success': 'OK',
        'message': 'Data pair <x:y> added correctly'
    }
    return jsonify(response)


@app.route("/api/list")
def list():
    data = [
        {'x': 'a', 'y': '2'},
        {'x': 'b', 'y': '4'},
        {'x': 'c', 'y': '6'}
    ]
    response = {
        'success': 'OK',
        'data': data
    }
    return jsonify(response)


@app.route("/api/infer", methods=['GET', 'POST'])
def infer():
    response = interface.on_infer(request.json['infer_x'])
    return jsonify(response)


if __name__ == '__main__':
    pass

