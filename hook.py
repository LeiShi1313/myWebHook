from flask import Flask, request
import json

HOST = '0.0.0.0'
PORT - 9700

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
    data = json.loads(request.data)
    if 'commits' in data:
        print "New commit by: {}".format(data['commits'][0]['author']['name'])
    else:
        print data

    return "OK"

if __name__ == '__main__':
   app.run(host=HOST, port=PORT)
