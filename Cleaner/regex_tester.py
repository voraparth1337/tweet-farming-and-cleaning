import re

subject = ' 892378180379709440(1)Jaipur http://t.co/miEYQ1EZZ 4#jaipur #India #voyage #Travel  -@- http://t.co/miEYQ1EZZ'
result = re.sub(r"http\S+", "URL", subject)

print(result)