import json
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

DATA_FILE = '.data.json'


def loadnodes():
    try:
        with open(".data.json", 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        data = []

    if not isinstance(data, list):
        data = [] 

    return data

    

def send_data():
    data = loadnodes()
    return jsonify(data)



@app.route('/get_data', methods=['GET'])
def get_data():
    data = loadnodes()
    return jsonify(data)


@app.route('/write_data', methods=['POST'])
def gennode():
    new_data = request.json
    data = loadnodes()

    max_id = max([item['id'] for item in data], default=0)

    new_data["id"] = max_id + 1

    data.append(new_data)
    with open(".data.json", 'w') as file:
        json.dump(data, file, indent=4)
    return jsonify({'id': max_id+1})


@app.route('/del_data', methods=['POST'])
def delnode():
    data = loadnodes()
    index_data = request.json
    index = index_data['index']
    print(index)
    if index >= 0:
        del data[int(index)]
        with open(".data.json", 'w') as file:
            json.dump(data, file, indent=4)
        id = int(index) + 1
        response = {'message': f'Entry: {id}, deleted!'}
    else:
        response = {'message': 'Index not provided'}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')