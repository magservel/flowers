from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/train")
def train():
    response = {
        'success': 'OK',
        'message': 'Model trained correctly with accuracy of 95.6%'
    }
    return jsonify(response)


@app.route("/api/add", methods=['GET', 'POST'])
def add():
    response = {
        'success': 'OK',
        'message': 'Data pair <x:y> added correctly'
    }
    return jsonify(response)


@app.route("/api/list")
def list():
    data = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    response = {
        'success': 'OK',
        'data': data
    }
    return jsonify(response)


@app.route("/api/infer", methods=['GET', 'POST'])
def infer():
    result = 1
    response = {
        'success': 'OK',
        'result': result
    }
    return jsonify(response)


if __name__ == '__main__':
    pass

