from flask import Flask
from flask import jsonify
from flask import request
from flask import after_this_request
from flask_cors import CORS
from flask_cors import cross_origin
from get_compressed import get_message

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'


cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods = ['GET', 'POST'])
@cross_origin(origin='/*',headers=['Content- Type','Authorization'])
def get_response():

    if request.method == 'GET':
        response = jsonify({'text': "Send POST data!"})
        return response
    elif request.method == 'POST':

        #tt = request.args.get('text')
        tt = request.get_json()
        text = str(get_message(tt['text']))
        response = jsonify({'text': text})
        #response = text
        return response
