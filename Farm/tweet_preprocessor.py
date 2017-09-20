import preprocessor as p
import re

p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.RESERVED, p.OPT.NUMBER, p.OPT.HASHTAG)
'''URL	p.OPT.URL
Mention	p.OPT.MENTION
Hashtag	p.OPT.HASHTAG
Reserved Words	p.OPT.RESERVED
Emoji	p.OPT.EMOJI
Smiley	p.OPT.SMILEY
Number	p.OPT.NUMBER  
'''

URL_PATTERN=re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
HASHTAG_PATTERN = re.compile(r'#\w*')
MENTION_PATTERN = re.compile(r'@\w*')
RESERVED_WORDS_PATTERN = re.compile(r'^(RT|FAV)')
NUMBERS_PATTERN = re.compile(r"(^|\s)(\-?\d+(?:\.\d)*|\d+)")

text = '#MotoG5sPlusLaunch at 12:15 PM today!! Gear up to find your focus & unleash your creativity. http://bit.ly/2ge1cSm! #happy'

a = p.clean(text)
print(a)


p.set_options(p.OPT.URL, p.OPT.HASHTAG)
parsed_tweet = p.parse(text)

print(parsed_tweet.hashtags)

print(parsed_tweet.urls[0])

