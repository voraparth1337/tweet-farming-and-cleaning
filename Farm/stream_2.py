
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'ij5etlAahSOEf4pccYAsdOIHb'
consumer_secret = 'c1Unl0eSZrI1dqjKcb6QqGiaucnSPhsgrrgJHz3oxWeUCbFu7p'
access_token = '970395806-h0JliTZVle6tWc6xnN2s4Kcn2ElAi2t3FUwZIJVv'
access_secret = 'qu9jNve0TvFCzbwcPETUMPVQRDFHdwcopaEhb10sGCq00'


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#angry', '#annoyed', '#irritated'])
