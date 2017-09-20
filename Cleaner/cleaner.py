import re

tweet_id_regex = re.compile(r'[0-9]+')
tweet_end_regex = re.compile(r'-@-')
tweet_url_regex = re.compile(r"http\S+")
tweet_username_regex = re.compile('(?<=^|(?<=[^a-zA-Z0-9-_\\.]))@([A-Za-z]+[A-Za-z0-9_]+)')

FILENAME = 'india.txt'
OUTPUT = 'india_clean.txt'

final = []

with open(FILENAME, 'r') as f_read, open(OUTPUT, 'w') as f_write:
    data = ''.join(line.rstrip() for line in f_read)
    data = data.split(sep='-@-')
    for item in data[0:-1]:
        temp = item.split(sep='(1)')
        Id = temp[0]
        Tweet = temp[1]
        string = Id + ':- ' + Tweet + '\n'
        string = re.sub(tweet_url_regex, "URL", string)
        string = re.sub(tweet_username_regex, "USERID", string)

        f_write.write(string)

f_read.close()
