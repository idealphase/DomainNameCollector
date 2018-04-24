domains = list()
with open("37_specific_domain_name_for_test.txt") as f:
    domains = f.read().split('\n')[:-1]

choices = list()
with open("../../script/filtered_from_4_generator.txt") as f:
    choices = f.read().split('\n')[:-1]

with open("filtered_from_4_generator_only_37_domain.txt",'w') as f:
    for choice in choices:
        temp = choice.split(' ')
        if temp[2] in domains:
            f.write(choice+'\n')
