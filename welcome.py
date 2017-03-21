from aylienapiclient import textapi
import os
from flask import Flask
import json
import webbrowser
import json
import cgi
import urllib.error, urllib.parse
import blockspring

client = textapi.Client("ede14ddd", "e9ae2130310ebe48fa5df1e6ae322bfa")

sentimentRaw = client.Sentiment({'text': 'John is a very good football player!'})

# print sentimentRaw

print "\n******************************** Sentiment Analysis \n"

url = 'http://edition.cnn.com/2017/03/14/europe/netherlands-refugees-wilders-we-are-here/index.html'
sentimentURL = client.Sentiment({'url': url})
for key, value in sentimentURL.iteritems():
    if not key == 'text':
         print key, " : ", value


print "\n******************************** Summarize \n"

summary = client.Summarize({'url': url, 'sentences_number': 3})
for sentence in summary['sentences']:
  print sentence

print "\n******************************** Entities \n"

entities = client.Entities({"url": url})
for type, values in entities['entities'].iteritems():
  print type,', '.join(values)

print "\n******************************** Hashtags\n"

hashtags = client.Hashtags({"url": url})
print ', '.join(hashtags['hashtags'])

print "\n******************************** Classifying by Taxonomy\n"

classifications = client.ClassifyByTaxonomy({"url": url, "taxonomy": "iab-qag"})
for category in classifications['categories']:
  print category


app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/search')
def Search():
    return app.send_static_file('search.html')

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=int(port))
    app.run(host='127.0.0.1', port=int(port))






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
  input1=str(request.form['input'])

  link = "http://money.cnn.com/quote/quote.html?symb=FIT";
  print("user input",input1)

  parameters = {"url": input1}
  language = call_api("language", parameters)

  parameters = {"url": input1}
  sentiment = call_api("sentiment", parameters)

  parameters = {"url": input1}
  hashtags = call_api("hashtags", parameters)

  parameters = {"url": input1}
  summarize = call_api("summarize", parameters)


  info = {'language':language,'sentiment':sentiment,'hashtags':hashtags, 'input1':input1}

  #return app.send_static_file('stock.html')
  #return jsonify(result=json.dumps(info))
  return jsonify(result=info)

# get link variable from js
# @app.route('/postmethod', methods = ['POST'])
# def getData():
#     jsdata = request.form['javascript_data']
#     return jsdata


# @app.route('/search', methods = ['GET', 'POST'])
# def Search():
# #	return app.send_static_file('stock.html')
#   # link="jgjgjg"
#  # link = request.POST.get('javascript_data')
#  # print (link)
#   link = "http://money.cnn.com/quote/quote.html?symb=FIT";

#   parameters = {"url": link}
#   language = call_api("language", parameters)

#   parameters = {"url": link}
#   sentiment = call_api("sentiment", parameters)

#   parameters = {"url": link}
#   hashtags = call_api("hashtags", parameters)



#   info = {'language':language,'sentiment':sentiment,'hashtags':hashtags}

#   return json.dumps(info)

def getUserInput():
  form = web.input(name="Search")
  greeting = "%s" % (form.name)
 # return render.index(name = name)
  return app.send_static_file('stock.html')

