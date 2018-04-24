import subprocess as sub
domains = list()
with open("./added_4banking_domains.txt") as f:
    domains = f.read().split('\n')[:-1]

print "[+] Number of whole domain is ",len(domains)
i = 0
with open("result_from_urlcrazy_added_4banking.txt","a") as f:
    while i < range(len(domains)):
        try:
            output = sub.check_output(['./urlcrazy',domains[i]])
        except sub.CalledProcessError as e:
            output = e.output
        f.write(output)
        print "[+] Done %d of %d" %(i+1,len(domains))
	i+=1
print "[+] Done whole task"
