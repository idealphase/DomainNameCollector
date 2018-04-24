import datetime
dnstwist = list()
with open("../dnstwist/result/filtered_result_from_dnstwist.txt") as f:
    dnstwist = f.read().split('\n')[:-1]
print "[+] Read dnstwist completely"
urlcrazy = list()
with open("../urlcrazy/result/filtered_result_from_urlcrazy.txt") as f:
    urlcrazy = f.read().split('\n')[:-1]
print "[+] Read urlcrazy completely"
typofinder = list()
with open("../typofinder/TypoMagic/result/formatted_result_from_typofinder.txt") as f:
    typofinder = f.read().split('\n')[:-1]
print "[+] Read typofinder completely"
typogenerator = list()
with open("../typogenerator/cmd/typogen/result/formatted_result_from_typogenerator.txt") as f:
    typogenerator = f.read().split('\n')[:-1]
print "[+] Read typogenerator completely"

with open("formatted_result_from_4_generator.txt","w") as f:
    ts = datetime.datetime.now()
    print "[+] Start read dnstwist ..."
    for d in dnstwist:
        if d in urlcrazy:
            if d in typofinder:
                if d in typogenerator:
                    temp = d+" 15\n"
                    f.write(temp)
                    urlcrazy.remove(d)
                    typofinder.remove(d)
                    typogenerator.remove(d)
                else:
                    temp = d+" 14\n"
                    f.write(temp)
                    urlcrazy.remove(d)
                    typofinder.remove(d)
            else:
                if d in typogenerator:
                    temp = d+" 13\n"
                    f.write(temp)
                    urlcrazy.remove(d)
                    typogenerator.remove(d)
                else:
                    temp = d+" 12\n"
                    f.write(temp)
                    urlcrazy.remove(d)
        else:
            if d in typofinder:
                if d in typogenerator:
                    temp = d+" 11\n"
                    f.write(temp)
                    typofinder.remove(d)
                    typogenerator.remove(d)
                else:
                    temp = d+" 10\n"
                    f.write(temp)
                    typofinder.remove(d)
            else:
                if d in typogenerator:
                    temp = d+" 9\n"
                    f.write(temp)
                    typogenerator.remove(d)
                else:
                    temp = d+" 8\n"
                    f.write(temp)
    print "[+] Start read urlcrazy"
    for d in urlcrazy:
        if d in typofinder:
            if d in typogenerator:
                temp = d+" 7\n"
                f.write(temp)
                typofinder.remove(d)
                typogenerator.remove(d)
            else:
                temp = d+" 6\n"
                f.write(temp)
                typofinder.remove(d)
        else:
            if d in typogenerator:
                temp = d+" 5\n"
                f.write(temp)
                typogenerator.remove(d)
            else:
                temp = d+" 4\n"
                f.write(temp)
    print "[+] Start read typofinder"
    for d in typofinder:
        if d in typogenerator:
            temp = d+" 3\n"
            f.write(temp)
            typogenerator.remove(d)
        else:
            temp = d+" 2\n"
            f.write(temp)
    print "[+] Start read typogenerator"
    for d in typogenerator:
        temp = d+" 1\n"
        f.write(temp)
tf = datetime.datetime.now()
print "[+] Elapsed time",tf-ts
print "[+] Complete all task !"
'''
