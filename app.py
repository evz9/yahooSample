#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

import matplotlib.pyplot as plt
import pandas as pd  # this is how I usually import pandas
import sys  # only needed to determine Python version number
import matplotlib  # only needed to determine Matplotlib version number
import nltk
from azureml import Workspace

# Flask app should start in global layout
app = Flask(__name__)

ws = Workspace(
    workspace_id='84e33ccc8d6f4d5b929e023b32ff3d22',
    authorization_token='f861df67af474dac8cff8ff8b0fd01fa',
    endpoint='https://studioapi.azureml.net'
)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    sum_bach = ws.datasets['sum_bach.csv']
    sum_bach_frame = sum_bach.to_dataframe()

    res = processRequest(req, sum_batch_frame)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req, sbf):
    if req.get("result").get("parameters").get("role") == "Salesman":
        return {
            "speech": "Top Skills: General Sales, General Sales Practices, Merchandising",
            "displayText": "you typed in jibberish this make it through",
            # "data": data,
            # "contextOut": [],
            "source": "apiai-weather-webhook-sample"
            }
    if req.get("result").get("parameters").get("role") == "Nurse Practitioner":
        return {
            "speech": "Top Skills: Basic Patient Care, Medical Support, General Medicine",
            "displayText": "Top Skills: Basic Patient Care, Medical Support, General Medicine",
            # "data": data,
            # "contextOut": [],
            "source": "apiai-weather-webhook-sample"
            }
    else:
        return {
            "speech":"lawl",
            "displayText": "idk",
            # "data": data,
            # "contextOut": [],
            "source": "apiai-weather-webhook-sample"
            }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
