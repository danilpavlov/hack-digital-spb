import os
from flask import Flask, request, jsonify
from parser import parse_etu
from filter_wrapper import FilterWrapper
from flask_cors import CORS



data_url = 'backend/src/filter/data/Данные приёмной кампании.csv'
profs_url = 'backend/src/filter/data/prof.csv'
app = Flask(__name__)
CORS(app, support_credintials=True)
if not os.path.exists(profs_url):
    parse_etu()

filter_wrap = FilterWrapper(data_url, profs_url)

@app.route('/', methods=['POST', "GET"])
def get_documents():
    if request.method == 'POST' and request.is_json:
        print('wjwjwjwj')
        abiture_data = request.json
        abiture_data['scores'] = [int(score) for score in abiture_data.get('scores', [])]
        documents = filter_wrap.get_documents(abiture_data)
        return jsonify(documents)

    elif request.method == 'GET':
        return filter_wrap.get_profs()

    else:
        return 'Invalid request', 400
    




if __name__ == '__main__':
    app.run(port=5001)
