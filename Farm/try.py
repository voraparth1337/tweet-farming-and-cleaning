import pandas as pd
import os
import json


folder_csv = 'data_csv/'
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
tweets['id'] = list(map(lambda tweet: tweet['id'], tweets_data))
tweets['id_str'] = list(map(lambda tweet: tweet['id_str'], tweets_data))
tweets['text'] = list(map(lambda tweet: tweet['text'].strip().replace('\n',' '), tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['favorite_count'] = list(map(lambda tweet: tweet['favorite_count'], tweets_data))
tweets['retweet_count'] = list(map(lambda tweet: tweet['retweet_count'], tweets_data))


tweets = tweets[tweets['lang'] == 'en' ]

csv_file_name = input('Output CSV file name ? \n')

tweets_output_data_path = folder_csv + csv_file_name

try:
    os.remove(tweets_output_data_path)
except OSError:
    pass

tweets.to_csv(tweets_output_data_path,index=False, index_label= False, header = True, encoding='utf-8')


