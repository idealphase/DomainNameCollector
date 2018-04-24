with open("formatted_result_from_typofinder.txt") as f:
    lines = f.read().split('\n')[:-1]

with open("temp.txt","w") as f:
    for line in lines:
        temp = line.split(' ')
        try:
            temp2 = ""
            if temp[0]=="homoglyph_confusables" or temp[0]=="additional_homoglyph":
                temp2 = "Homoglyph "+temp[1]+" "+temp[2]+"\n"
            elif temp[0] == "bitflipstring":
                temp2 = "Bitsquatting "+temp[1]+" "+temp[2]+"\n"
            elif temp[0] == "miskeyed_addition":
                temp2 = "Insertion "+temp[1]+" "+temp[2]+"\n"
            elif temp[0] == "miskeyed" or temp[0] == "replace_i_l_1_o_0":
                temp2 = "Replacement "+temp[1]+" "+temp[2]+"\n"
            elif temp[0] == "ings_and_plurals" or temp[0] =="ings_and_plurals_then_replace_i_l_1_o_0":
                temp2 = "Addition "+temp[1]+" "+temp[2]+"\n"
            elif temp[0] == "missing_character":
                temp2 = "Omission "+temp[1]+" "+temp[2]+"\n"
            elif temp[0] == "extra_dot_doppelgangers" or temp[0]=="subdomain_doppelgangers":
                temp2 = "Subdomain "+temp[1]+" "+temp[2]+"\n"
            elif temp[0] == "transposed_character":
                temp2 = "Transposition "+temp[1]+" "+temp[2]+"\n"
            elif temp[0] == "duplicate_character":
                temp2 = "Repetition "+temp[1]+" "+temp[2]+"\n"
            elif temp[0] == "miskeyed_sequence":
                temp2 = "Various "+temp[1]+" "+temp[2]+"\n"
            else:
                temp2 = line+'\n'
        except:
            pass
        f.write(temp2)
