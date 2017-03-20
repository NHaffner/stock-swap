from aylienapiclient import textapi
import os
import tweepy

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
    app.run(host='0.0.0.0', port=int(port))
    # app.run(host='127.0.0.1', port=int(port))





#
# # Consumer keys and access tokens, used for OAuth
# consumer_key = 'V3SAhL1fkIzymT4KM6bbKgkPT'
# consumer_secret = 'iRAl5TwShbnKu7L02TPmpqWFU9VFa6UuBlutT3BwVnwzAgHeFq'
# access_token = '841426734792744960-dIODXZtb1LTBocOY8rinMU0QT6lzmBF'
# access_token_secret = 'HgTwS9KJ1vGic0WzQBJlgIJHVqlUS5V360R9RcQ9ZZcx9'
#
# # OAuth process, using the keys and tokens
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# # Creation of the actual interface, using authentication
# api = tweepy.API(auth)
#
# # Sample method, used to update a status
# api.update_status('Hello Python Central!')

#!/usr/bin/env python
# from TwitterSearch import *
# try:
#     tso = TwitterSearchOrder() # create a TwitterSearchOrder object
#     tso.set_keywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
#     tso.set_language('de') # we want to see German tweets only
#     tso.set_include_entities(False) # and don't give us all those entity information
#
#     # it's about time to create a TwitterSearch object with our secret tokens
#     ts = TwitterSearch(
#         consumer_key = 'aaabbb',
#         consumer_secret = 'cccddd',
#         access_token = '111222',
#         access_token_secret = '333444'
#      )
#
#      # this is where the fun actually starts :)
#     for tweet in ts.search_tweets_iterable(tso):
#         print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
#
# except TwitterSearchException as e: # take care of all those ugly errors if there are some
#     print(e)