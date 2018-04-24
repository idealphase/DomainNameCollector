import idna

with open("filtered_result_from_dnstwist.txt") as f:
    lines = f.read().split('\n')[:-1]

for line in lines:
    temp = line.split(' ')
    if temp[0] == "Homoglyph":
        print temp[0],idna.encode(temp[1].decode('utf-8')),temp[2]
    else:
        print line
