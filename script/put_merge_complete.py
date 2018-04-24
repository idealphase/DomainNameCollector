from elasticsearch import Elasticsearch
import arrow
es = Elasticsearch(['localhost'],port=9199)
print "[+] Elasticsearch object created"
domains = list()

with open("./merge_complete_with_source.txt") as f:
    domains = f.read().split('\n')
    #delete last empty element
    domains = domains[:-1]
print "[+] Read file completed"

for domain in domains:
    temp = domain.split(" ")    
    print temp[0],temp[1]
    doc = {'domain': temp[0],'source':temp[1],'created_date':arrow.now().format('YYYY-MM-DD')}
    res = es.index(index='normal_domain_name',doc_type='doc*',body=doc)
