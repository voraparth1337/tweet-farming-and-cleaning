import re

tweet_id_regex = re.compile(r'[0-9]+')
tweet_end_regex = re.compile(r'-@-')
tweet_url_regex = re

FILENAME = 'india.txt'
OUTPUT = 'india_clean.txt'

final = []


with open(FILENAME, 'r') as f_read, open(OUTPUT, 'w') as f_write:
    data = ''.join(line.rstrip() for line in f_read)
f_read.close()

data = data.split(sep='-@-')

for item in data:
    print(item)