import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

consumer_key = 'MM4uOMgZbAa8vr2REvSLEvEi9'
consumer_secret = '8lIWExfSVb5vPYMdD4DevBzxB4NHGpYKU3Cabpj9Xmi67F5PSr'
access_token = '970395806-i2tVbzdRgO91Zdxvho6YugkjAXfPcaAXJcszqA60'
access_secret = '5hlvIOqm8mAk3Kjcat3g4SOZAdv2KPzjnsybQPFE2s7sy'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweet_json/5_9_17_1_sad.txt', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))

        return True

    def on_error(self, status):
        print(status)
        return True


while True:
    try:
        twitter_stream = Stream(auth, MyListener())
        twitter_stream.filter(track=['#bored','#sad','#depressed','#depress','#lonely','#rip','#missyou','#tragedy'])

    except:
        print('AGAIN ')
