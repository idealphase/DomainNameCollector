import codecs
lines = list()
with open("temp.txt") as f:
    lines = f.read().split('\n')
    lines = lines[:-1]
print "[+] Read file complete"

for line in lines:
    temp = line.split(',')
    if temp[0] != "Homoglyph":
        for domain in temp[2:len(temp)]:
            #print domain.rstrip(']').lstrip('[')
            print temp[0],domain.rstrip(']').lstrip('['),temp[1]
    else:
        for domain in temp[2:len(temp)]:
            temp2 = domain.rstrip(']').lstrip('[')
            try:
                temp3 = unicode(temp2,"utf-8")
            except:
                raise 
            try:
                temp4 = codecs.encode(temp3,"idna")
            except:
                pass
            print temp[0],temp4,temp[1]
