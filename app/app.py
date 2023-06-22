import json
import re

import flask
import requests
from flask import Flask
app = Flask(__name__)

def getJokesIds():
    list = []
    for i in range(1, 6):
        response = requests.get(f'http://bash.org.pl/latest/?page={i}')
        t = re.findall('<div id="d[0-9]{1,7}" class="q post">', str(response.content))
        string=''
        for m in t:
            string += ' ' + m
        x = re.findall('[0-9]{1,7}', string)
        list = list + x

    return list

def getJokeContent(jokeId):
    response = requests.get(f'http://bash.org.pl/{jokeId}')
    x = re.findall('<div class="quote post-content post-body">(.*?)<\/div>', str(response.content))
    return str(x)



@app.route('/jokes', methods=['GET'])
def index():
    jokes_string = '''
    {
        "jokes": [
        
        ]
    }
    '''
    data = json.loads(jokes_string)
    l = getJokesIds()
    x =''
    for i in l:
        x = x + getJokeContent(i)
        data["jokes"].append({"jokeId":str(i), "jokeContent":getJokeContent(i)})
    return flask.jsonify(data)

app.run(host='0.0.0.0')