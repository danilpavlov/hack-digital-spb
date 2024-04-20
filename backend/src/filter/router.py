import os
from flask import Flask, request, jsonify
from parser import parse_etu
from filter_wrapper import FilterWrapper

app = Flask(__name__)

data_url = 'backend/src/filter/data/Данные приёмной кампании.csv'
profs_url = 'backend/src/filter/data/prof.csv'

if not os.path.exists(profs_url):
    parse_etu()

filter_wrap = FilterWrapper(data_url, profs_url)

@app.route('/', methods=['GET'])
def get_documents():
    if request.method == 'GET' and request.is_json:
        abiture_data = request.json
        documents = filter_wrap.get_documents(abiture_data)
        return jsonify(documents)
    else:
        return 'Invalid request', 400

if __name__ == '__main__':
    app.run(port=5001)
