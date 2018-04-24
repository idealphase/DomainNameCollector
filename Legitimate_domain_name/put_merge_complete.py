from elasticsearch import Elasticsearch
from datetime import datetime
es = Elasticsearch()
print "[+] Elasticsearch object created"
domains = list()

with open("./merge_complete_with_source.txt") as f:
    domains = f.read().split('\n')[:-1]
print "[+] Read file completed"

for domain in domains:
    temp = domain.split(" ")    
    print temp[0],temp[1]
    doc = {'domain': temp[0],'source':temp[1],'date_created':datetime.now()}
    res = es.index(index='legitimate_domain_name',doc_type='doc',body=doc)
