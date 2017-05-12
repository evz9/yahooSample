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

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    # print(res)
    r = {
        "speech": "Please let this work",
        "displayText": "Please let this work",
        "data": "data",
        "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }
    r.headers['Content-Type'] = 'application/json'
    return r


