from elasticsearch import Elasticsearch
import arrow
es = Elasticsearch(['localhost'],port=9199)
print "[+] Elasticsearch object created"
domains = list()

with open("./filtered_result_from_4_generator.txt") as f:
    domains = f.read().split('\n')[:-1]
print "[+] Read file completed"

i = 0
for domain in domains:
    temp = domain.split(" ")    
    doc = {'fuzzer': temp[0],'domain':temp[1],'original':temp[2],'generator':temp[3]}
    res = es.index(index='domain_name_typosquatting',doc_type='doc*',body=doc)
    i+=1
    if i%10000 == 0:
        print "[+] Round ",i
