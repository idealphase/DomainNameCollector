domains14 = list()
with open("14_domain_typo_that_exist_in_normal_domain.txt") as f:
    domains14 = f.read().split("\n")
    domains14 = domains14[:-1]

dnstwist_domains = list()
with open("formatted_result_from_typofinder.txt") as f:
    dnstwist_domains = f.read().split("\n")
    dnstwist_domains = dnstwist_domains[:-1]

with open("filtered_result_from_typofinder.txt","w") as f: 
    for dnstwist_domain in dnstwist_domains:
        temp = dnstwist_domain.split()
        found = False
        for domains1 in domains14:
            if domains1 == temp[1]:
                print "[+] Found",domains1,"in dnstwist result"
                found= True
        if found == False: 
            temp2 = temp[0]+" "+temp[1]+" "+temp[2]+"\n"
            f.write(temp2)
print "[+] Whole task done :: result in filtered_result_from_dnstwist.txt"
