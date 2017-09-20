import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

consumer_key = 'ij5etlAahSOEf4pccYAsdOIHb'
consumer_secret = 'c1Unl0eSZrI1dqjKcb6QqGiaucnSPhsgrrgJHz3oxWeUCbFu7p'
access_token = '970395806-h0JliTZVle6tWc6xnN2s4Kcn2ElAi2t3FUwZIJVv'
access_secret = 'qu9jNve0TvFCzbwcPETUMPVQRDFHdwcopaEhb10sGCq00'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweet_json/5_9_17_1_angry.txt', 'a') as f:
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
        twitter_stream.filter(track=['#furious','#bothered','#annoying','#mad','#hateit','#irritated', '#annoyed', '#outraged', '#galled', '#provoked', '#irked','#tetchy', '#dyspeptic', '#ranting', '#wrathful', '#seething', '#infuriated', '#angry', '#livid', '#aggrieved', '#crabby', '#incandescent', '#choleric', '#frenzied', '#vexed', '#raving', '#irate', '#incensed', '#splenetic', '#displeased', '#piqued', '#enraged', '#waspish', '#antagonistic', '#resentful', '#testy', '#exasperated', '#fuming', '#raging'])
    
    except:
        print('AGAIN ')

