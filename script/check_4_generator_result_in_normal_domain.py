import datetime
normal_domains = list()
with open ("590_legitimate_domain_name_with_source.txt") as f:
    normal_domains = f.read().split("\n")[:-1]
print normal_domains
print "[+] Normal domain have %d domains" %(len(normal_domains))

four_generator_domains = list()
with open ("formatted_result_from_4_generator.txt") as f:
    four_generator_domains = f.read().split("\n")[:-1]
print "[+] Four generator have %d domains" %(len(four_generator_domains))

ts = datetime.datetime.now()
with open("filtered_from_4_generator.txt","w") as f:
    for four_generator_domain in four_generator_domains:
        temp = four_generator_domain.split(' ')   
        if temp[1] in normal_domains:
            print "[-] Found ",temp[1],"in normal_domains"
        else:
            f.write(four_generator_domain+'\n')
tf = datetime.datetime.now()
print "[+] elapsed time is",tf-ts
