import preprocessor as p

text = '#MotoG5sPlusLaunch at 12:15 PM today!! Gear up to find your focus & unleash your creativity. http://bit.ly/2ge1cSm!'

a = p.clean(text)
print(a)

parsed_tweet = p.parse(text)

print(parsed_tweet.hashtags)

print(parsed_tweet.urls)

