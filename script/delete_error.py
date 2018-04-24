with open("formatted_result_from_4_generator.txt") as f:
    lines = f.read().split('\n')
    lines = lines[:-1]

for line in lines:
    temp = line.split(' ')
    try:
        print temp[0],temp[1],temp[2],int(temp[3])
    except:
        pass
