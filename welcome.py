#Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify,request
import json
import webbrowser
import json
import cgi
import urllib.error, urllib.parse


APPLICATION_ID = "67c4cb60"
APPLICATION_KEY = "a2a95e80b71539e9d1c4694a6199f107"

app = Flask(__name__)

def call_api(endpoint, parameters):
  url = 'https://api.aylien.com/api/v1/' + endpoint
  headers = {
      "Accept":                             "application/json",
      "Content-type":                       "application/x-www-form-urlencoded",
      "X-AYLIEN-TextAPI-Application-ID":    APPLICATION_ID,
      "X-AYLIEN-TextAPI-Application-Key":   APPLICATION_KEY
  }
  opener = urllib.request.build_opener()
  request = urllib.request.Request(url,urllib.parse.urlencode(parameters).encode('utf-8'), headers)
  response = opener.open(request);
  return json.loads(response.read().decode())

@app.route('/')
@app.route('/index.html')
def Welcome():
    return app.send_static_file('index.html')


@app.route('/stock', methods=['POST'])
def Stock():
  inputLink=str(request.form['input'])
  if inputLink == 'Starbucks':
    input1 = "http://www.barrons.com/articles/five-reasons-starbucks-should-rebound-this-year-1490033222"

  if inputLink == 'Netflix':
    input1 = 'http://www.valuewalk.com/2017/03/netflix-stock-price-target-international/'

  parameters = {"url": input1}
  language = call_api("language", parameters)

  parameters = {"url": input1}
  sentiment = call_api("sentiment", parameters)

  parameters = {"url": input1}
  hashtags = call_api("hashtags", parameters)

  parameters = {"url": input1}
  summarize = call_api("summarize", parameters) 


  info = {'language':language,'sentiment':sentiment,'hashtags':hashtags, 'summarize': summarize, 'input1':input1}

  return jsonify(result=info)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(port))
