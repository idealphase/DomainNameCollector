import subprocess as sub
domains = list()
with open("./added_4banking_domains.txt") as f:
    domains = f.read().split('\n')
    domains = domains[:-1]

print "[+] Number of whole domain is ",len(domains)
with open("result_4banking_from_dnstwist.txt","a") as f:
    for domain in domains:
        output = sub.check_output(["./dnstwist.py",domain])
        f.write(output)
        print "[+] Done %s" %(domain)
print "[+] Done whole task"
