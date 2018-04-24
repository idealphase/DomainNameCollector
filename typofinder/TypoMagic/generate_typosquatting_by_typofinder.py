import typogen
_typogen = typogen.typogen()
import datetime

domains = list()
with open("./merge_complete.txt") as f:
    domains = f.read().split('\n')
    domains = domains[:-1]

ts = datetime.datetime.now()
for domain in domains:
    typo_domain = _typogen.generatetyposv2(domain,"gb",True,100,False,True,True,True,False,False,100)
tf = datetime.datetime.now()
print(tf-ts)
