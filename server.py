from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json  # Get JSON data from the request
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        result = b+a
        return jsonify({'result': result})
    else:
        return jsonify({'eror': 'Missing parameters'}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json  # Get JSON data from the request
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        result = a - b
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing parameters'}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
