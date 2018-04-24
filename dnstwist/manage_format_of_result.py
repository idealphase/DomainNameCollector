lines = list()
with open("result_4banking_from_dnstwist.txt") as f:
    lines = f.read().split('\n') [:-1]

original = ""
with open("formatted_result_4banking_from_dnstwist.txt","w") as f:
    for line in lines:
        temp = line.split()
        if temp[0] == "Original*":
            original = temp[1]
            print "[+] Changed original to",original
        else:
            temp2 = ""+temp[0]+" "+temp[1]+" "+original+'\n'
            f.write(temp2)
