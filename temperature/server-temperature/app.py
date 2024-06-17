from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['Temperature']
collection = db['sensorTemperatures']

@app.route('/', methods=['GET'])
def root():
    return '<html><h1>Miku-Sensor. Temperatures: </h1></html>'


@app.route('/temperatures', methods=['GET'])
def get_temperatures():
    documents = list(collection.find())
    for i in documents:
        i['_id'] = str(i['_id'])
    return documents, 200

@app.route('/register_temp', methods=['POST'])
def register_temp():
    document = request.json
    if not document:
        return jsonify({'error': 'No data provided'}), 400
    #Validate data
    post_id = collection.insert_one(document).inserted_id
    return jsonify({'message':f'temperature messuare registered correctly {post_id}'}), 201


if __name__ == '__main__':
    app.run(port=5500,debug=True)