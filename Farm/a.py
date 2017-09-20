import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import multiprocessing

def _angry_():
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


def _happy_():
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
	            with open('tweet_json/5_9_17_1_happy.txt', 'a') as f:
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
	        twitter_stream.filter(track=['#relaxing','#peace','#calm','calm','#peaceful','#sleepy'])

	    except:
	        print('AGAIN ')


def _sad_():
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


def _excited_():
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
	            with open('tweet_json/5_9_17_1_excited.txt', 'a') as f:
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
	        twitter_stream.filter(track=['#excited','#happy','#veryhappy','#awesome','#amazing'])

	    except:
	        print('AGAIN ')



if __name__ == '__main__':
	print('Starting angry..')
	p = multiprocessing.Process(name='p', target=_angry_)
	
	print('Starting happy..')
	p1 = multiprocessing.Process(name='p1', target=_happy_)

	print('Starting sad..')
	p2 = multiprocessing.Process(name='p2', target=_sad_)

	print('Starting excited..')
	p3 = multiprocessing.Process(name='p3', target=_excited_)
	
	p.start()
	p1.start()
	p2.start()
	p3.start()