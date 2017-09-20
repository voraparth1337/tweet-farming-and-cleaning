# getting all tweets from a user
import tweepy
import re

# emoji removal pattern
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F917" # 
        u"\U0001F981" # lion
                           "]+", flags=re.UNICODE)

consumer_key = 'ij5etlAahSOEf4pccYAsdOIHb'
consumer_secret = 'c1Unl0eSZrI1dqjKcb6QqGiaucnSPhsgrrgJHz3oxWeUCbFu7p'
access_token = '970395806-h0JliTZVle6tWc6xnN2s4Kcn2ElAi2t3FUwZIJVv'
access_secret = 'qu9jNve0TvFCzbwcPETUMPVQRDFHdwcopaEhb10sGCq00'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

alltweets = []

api = tweepy.API(auth)

screen_name  = 'parth2351'

new_tweets = api.user_timeline(screen_name = screen_name,count=200)

alltweets.extend(new_tweets)

oldest = alltweets[-1].id - 1

while len(new_tweets) > 0:
    print("getting tweets before %s" % (oldest))

    # all subsiquent requests use the max_id param to prevent duplicates
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # update the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
# outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
outtweets = [tweet.text for tweet in alltweets]

for item in outtweets:
    text = item
    print(emoji_pattern.sub(r'', text).encode('utf-8')) # no emoji


