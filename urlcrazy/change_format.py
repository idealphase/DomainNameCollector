lines = list()
with open("./result_from_urlcrazy_added_4banking.txt") as f:
    lines = f.read().split('\n')[:-1]

with open("./formatted_result_4banking_from_urlcrazy.txt",'w') as f:
    for line in lines:
        temp = line.split(',')
        temp2 = ""
        try:
            temp2 = temp[0].replace(' ','_')+' '+temp[1]+' '+temp[len(temp)-1]+'\n'
        except:
            pass
        f.write(temp2)
