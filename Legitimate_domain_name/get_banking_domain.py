import re
from tld import get_tld
BankingDomains = list()
with open('./bot1.html') as f:
    temp = f.read()

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', temp)

with open('./banking_domains.txt','w') as f:
    for url in urls:
        res = get_tld(url,as_object=True)
        f.write(res.tld+'\n')
