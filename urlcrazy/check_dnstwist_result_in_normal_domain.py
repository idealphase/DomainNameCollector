normal_domains = list()
with open ("590_legitimate_domain_name_with_source.txt") as f:
    normal_domains = f.read().split("\n")[:-1]

dnstwist_domains = list()
with open ("formatted_result_from_urlcrazy.txt") as f:
    dnstwist_domains = f.read().split("\n")[:-1]

for dnstwist_domain in dnstwist_domains:
    temp = dnstwist_domain.split()   
    for normal_domain in normal_domains:
        temp2 = normal_domain.split()
        if temp[1] == temp2[0]:
            print "[*] Found ",temp[1],temp2[0],temp[2],temp[0]
