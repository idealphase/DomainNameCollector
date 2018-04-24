bank_domains = list()
with open("banking_domains.txt") as f:
    bank_domains = f.read().split("\n")
    bank_domains = bank_domains[:-1]

with open("merge_complete_with_source.txt","w") as f:
    for bank_domain in bank_domains:
        temp = bank_domain+" bot.or.th\n"
        f.write(temp)
print "[+] Added source to banking domain completely"

alexa_domains = list()
with open("thailand_alexa_top_500.txt") as f:
    alexa_domains = f.read().split("\n")
    alexa_domains = alexa_domains[:-1]

with open("merge_complete_with_source.txt","a") as f:
    for alexa_domain in alexa_domains:
        temp = alexa_domain+" alexa.com\n"
        f.write(temp)
print "[+] Added source to thailand alexa top 500 domain completely"
