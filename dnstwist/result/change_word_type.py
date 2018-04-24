with open("filtered_result_from_dnstwist.txt") as f:
    lines = f.read().split('\n')[:-1]

with open("temp.txt","w") as f:
    for line in lines:
        temp = line.split(' ')
        temp2 = ""
        if temp[0]=="Vowel-swap":
            temp2 = "Vowel_Swap "+temp[1]+" "+temp[2]+"\n"
        else:
            temp2 = line+'\n'
        f.write(temp2)
