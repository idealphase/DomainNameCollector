with open("filtered_result_from_urlcrazy.txt") as f:
    lines = f.read().split('\n')[:-1]

with open("temp.txt","w") as f:
    for line in lines:
        temp = line.split(' ')
        temp2 = ""
        if temp[0]=="Homoglyphs":
            temp2 = "Homoglyph "+temp[1]+" "+temp[2]+"\n"
        elif temp[0] == "Bit_Flipping":
            temp2 = "Bitsquatting "+temp[1]+" "+temp[2]+"\n"
        elif temp[0] == "Character_Insertion":
            temp2 = "Insertion "+temp[1]+" "+temp[2]+"\n"
        elif temp[0] == "Character_Replacement" or temp[0] == "Double_Character_Replacement":
            temp2 = "Replacement "+temp[1]+" "+temp[2]+"\n"
        elif temp[0] == "Singular_or_Pluralise":
            temp2 = "Addition "+temp[1]+" "+temp[2]+"\n"
        elif temp[0] == "Character_Omission":
            temp2 = "Omission "+temp[1]+" "+temp[2]+"\n"
        elif temp[0] == "Wrong_SLD":
            temp2 = "Subdomain "+temp[1]+" "+temp[2]+"\n"
        elif temp[0] == "Character_Swap":
            temp2 = "Transposition "+temp[1]+" "+temp[2]+"\n"
        elif temp[0] == "Character_Repeat":
            temp2 = "Repetition "+temp[1]+" "+temp[2]+"\n"
        else:
            temp2 = line+"\n"
        f.write(temp2)
