import re
ThailandTopAlexa500 = list()
with open('./html.txt','r') as f:
    temp=f.read()

with open('./thailand_alexa_top_500.txt','w') as f:
    for line in temp.split('\n'):
        if "<a href=\"/siteinfo/" in line: 
            f.write(line.split('/')[2].split("\"")[0]+"\n")
