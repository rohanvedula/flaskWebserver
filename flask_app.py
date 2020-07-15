from flask import Flask
from flask import jsonify
from flask import request
from flask import after_this_request
from flask_cors import CORS
from flask_cors import cross_origin
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize

def get_message(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq



    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

    return summary

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'


cors = CORS(app, resources={r"/*": {"origins": "*"}})

#@app.route('/')
def hello_world():
    return 'Hello from Flask!'

#@app.route('/')
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
