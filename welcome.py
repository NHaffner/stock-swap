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