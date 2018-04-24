from elasticsearch import Elasticsearch
from os import listdir
import json

es = Elasticsearch(['localhost'],port=9199)
print "[+] Elasticsearch object created"

BASE_DIRECTORY="/home/idealphase/"
year="2017"
for month in listdir(BASE_DIRECTORY+year):
    for day in listdir(BASE_DIRECTORY+year+'/'+month):
        for hour in listdir(BASE_DIRECTORY+year+'/'+month+'/'+day):
            for minute in listdir(BASE_DIRECTORY+year+'/'+month+'/'+day+'/'+hour):
                count = {'A':0,'CNAME':0,'AAAA':0,'NS':0,'PTR':0,'SOA':0,'MX':0,'TXT':0,'OTHER':0}
                for second in listdir(BASE_DIRECTORY+year+'/'+month+'/'+day+'/'+hour+'/'+minute):
                    #print year,month,day,hour,minute,second

                    with open(BASE_DIRECTORY+year+'/'+month+'/'+day+'/'+hour+'/'+minute+'/'+second) as f:
                        lines = f.read().split('\n')[:-1]
                        for line in lines:
                            json_line = json.loads(line)
                            try:
                                count[json_line['type']]+=1
                            except:
                                count['OTHER']+=1
                doc = {'timestamp':year+'-'+month+'-'+day+':'+hour+'-'+minute,'count':json.dumps(count)}
                print count
                res = es.index(index='count_type',doc_type='doc*',body=doc)


'''
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
'''
