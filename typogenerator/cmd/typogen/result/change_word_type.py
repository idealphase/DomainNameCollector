with open("formatted_result_from_typogenerator.txt") as f:
    lines = f.read().split('\n')[:-1]

with open("temp.txt","w") as f:
    for line in lines:
        temp = line.split(' ')
        temp2 = ""
        if temp[0]=="BitSquatting":
            temp2 = "Bitsquatting "+temp[1]+" "+temp[2]+"\n"
        elif temp[0]=="DoubleHit_[English]":
            temp2 = "Insertion "+temp[1]+" "+temp[2]+"\n"
        elif temp[0]=="Replace_[English]":
            temp2 = "Replacement "+temp[1]+" "+temp[2]+"\n"
        elif temp[0]=="Prefix":
            temp2 = "Addition "+temp[1]+" "+temp[2]+"\n"
        elif temp[0]=="VowelSwap":
            temp2 = "Vowel_Swap "+temp[1]+" "+temp[2]+"\n"
        else:
            temp2 = line+'\n'
        f.write(temp2)
