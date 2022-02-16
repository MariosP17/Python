from urllib.request import Request, urlopen
from scipy.stats import entropy
import pandas as pd

x= [ ]
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
l =str(data)
p = l.split(",")
b= str(p[0])
k = b.split(':')
round = k[1]
s = l.split('"randomness":', 1)
a =str(s[1])
f = a.split(",",1)
for s in f[0][1:-1]:
    x.append(s)
for i in range(19):
    round=int(round)-1
    req1 = Request('https://drand.cloudflare.com/public/'+str(round), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data1 = urlopen(req1).read()
    h =str(data1)
    j = h.split('"randomness":', 1)
    y =str(j[1])
    g = y.split(",",1)
    for s in g[0][1:-1]:
        x.append(s)
x = pd.Series(x)
result = entropy(x.value_counts(), base=2)
print('Η εντροπία των 20 τελευταίων τιμών έχει τιμή:',result)
