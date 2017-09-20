import pandas as pd
import os
import json


folder_csv = 'data_csv/new/'
folder_text = 'tweet_json/'

text_file_name = input('Enter file name with extension \n')
tweets_input_data_path = folder_text + text_file_name

tweets_file = open(tweets_input_data_path, "r")

tweets_data = []

for line in tweets_file:
    try:
        if 'created_at' not in line:
            pass
        else:
            tweet = json.loads(line)
            tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()

tweets_id = [t['id'] for t in tweets_data]
tweets_id_str = [t['id_str'] for t in tweets_data]
tweets_text = [t['text'] for t in tweets_data]
tweets_lang = [t['lang'] for t in tweets_data]
tweets_fav_count = [t['favorite_count'] for t in tweets_data]
tweets_rt_count = [t['retweet_count'] for t in tweets_data]
tweets_source = [t['source'] for t in tweets_data]
tweets_geo = [t['geo'] for t in tweets_data]
tweets_loc = [t['place'] for t in tweets_data]
hashtags = [hashtag['text'] for t in tweets_data for hashtag in t['entities']['hashtags'] ]
'''
tweets['id'] = list(map(lambda tweet: tweet['id'], tweets_data))
tweets['id_str'] = list(map(lambda tweet: tweet['id_str'], tweets_data))
tweets['text'] = list(map(lambda tweet: str(tweet['text'].strip().replace('\n',' ')), tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['favorite_count'] = list(map(lambda tweet: tweet['favorite_count'], tweets_data))
tweets['retweet_count'] = list(map(lambda tweet: tweet['retweet_count'], tweets_data))
tweets['source'] = list(map(lambda tweet: tweet['source'], tweets_data))
tweet_geo = [tweet['geo'] for tweet in tweets]
'''

tweets['id'] = tweets_id
tweets['id_str'] = tweets_id_str
tweets['text'] = tweets_text
tweets['lang'] = tweets_lang
tweets['fav_count'] = tweets_fav_count
tweets['rt_count'] = tweets_rt_count
tweets['source'] = tweets_source
tweets['geo'] = tweets_geo
tweets['loc'] = tweets_loc

tweets = tweets[tweets['lang'] == 'en' ]

csv_file_name = input('Output CSV file name ? \n')

tweets_output_data_path = folder_csv + csv_file_name

try:
    os.remove(tweets_output_data_path)
except OSError:
    pass


tweets.to_csv(tweets_output_data_path,index=False, index_label= False, header = True, encoding='utf-8')

tweets_output_data_path = folder_csv + csv_file_name + '.xlsx'

tweets.to_excel(tweets_output_data_path,encoding='utf-8')

print(hashtags)
