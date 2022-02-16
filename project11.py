from urllib.request import Request, urlopen
from scipy.stats import entropy
import pandas as pd

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
l =str(data)
s = l.split('"randomness":', 1)
a =str(s[1])
f = a.split(",",1)
num = int((f[0][-21:-1]), 16)
j = hex(num)[2:]
a= []
for s in j:
    a.append(s)
a = pd.Series(a)
result = entropy(a.value_counts(), base=2)
print('Η εντροπία των 20 τελευταίων ψηφίων "',j,'" έχει τιμή:',result)