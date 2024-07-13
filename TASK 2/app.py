from flask import Flask, jsonify
import json

app = Flask(__name__)

def read_data_from_file():
    with open('kafka_data.json', 'r') as f:
        data = [json.loads(line) for line in f]
    return data

@app.route('/data', methods=['GET'])
def get_data():
    data = read_data_from_file()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
