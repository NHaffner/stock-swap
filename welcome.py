from aylienapiclient import textapi
import os
from flask import Flask, jsonify


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

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
    # app.run(host='127.0.0.1', port=int(port))





# import json
# import urllib.request, urllib.error, urllib.parse
#
# APPLICATION_ID = 'ede14ddd'
# APPLICATION_KEY = 'e9ae2130310ebe48fa5df1e6ae322bfa'
#
# def call_api(endpoint, parameters):
#   url = 'https://api.aylien.com/api/v1/' + endpoint
#   headers = {
#       "Accept":                             "application/json",
#       "Content-type":                       "application/x-www-form-urlencoded",
#       "X-AYLIEN-TextAPI-Application-ID":    "ede14ddd",
#       "X-AYLIEN-TextAPI-Application-Key":   "e9ae2130310ebe48fa5df1e6ae322bfa",
#   }
#   opener = urllib.request.build_opener()
#   request = urllib.request.Request(url,
#     urllib.parse.urlencode(parameters).encode('utf-8'), headers)
#   response = opener.open(request);
#   return json.loads(response.read().decode())
#
# parameters = {"text": "What language is this sentence written in?"}
# language = call_api("language", parameters)
#
# parameters = {"text": "John is a very good football player!"}
# sentiment = call_api("sentiment", parameters)
#
# parameters = {"url": "http://www.bbc.com/news/health-29912877"}
# hashtags = call_api("hashtags", parameters)
#
# print("n")
# print("Text: %s " % (language["text"]))
# print("Language: %s (%F)" % (language["lang"], language["confidence"]))
# print("n")
# print("Text: %s " % (sentiment["text"]))
# print("Sentiment: %s (%F)" % (sentiment["polarity"], sentiment["polarity_confidence"]))
# print("n")
# print("Hashtags: %s " % (hashtags["hashtags"]))
# print("n")
# print("Text: %s " % (hashtags["text"]))