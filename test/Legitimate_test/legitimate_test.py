import time
import socket
with open("../../Legitimate_domain_name/590_legitimate_domain_name_with_source.txt") as f:
    domains = f.read().split('\n')[:-1]

print "[+] Start getaddrinfo"
for domain in domains:
    try:
        socket.getaddrinfo(domain,0,0,0,0)
    except:
        pass
print "[+] Done whole tasks"

