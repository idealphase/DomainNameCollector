import random
with open("filtered_from_4_generator_only_37_domain.txt") as f:
    choices = f.read().split('\n')[:-1]

with open("37_specific_domain_name_for_test.txt") as f:
    domains = f.read().split('\n')[:-1]

fuzzer_names = ["Homoglyph","Insertion","Bitsquatting","Subdomain","Addition","Replacement","Vowel_Swap",
"Wrong_TLD","Omission","Repetition","Transposition","Hyphenation","Various","Missing_Dot","Homophones",
"Common_Misspelling","Strip_Dashes"]

detail = dict()
for domain in domains:
    detail[domain] = {
            "domain_count": 0,
            "Homoglyph_count": 0,
            "Insertion_count": 0,
            "Bitsquatting_count": 0,
            "Subdomain_count": 0,
            "Addition_count": 0,
            "Replacement_count": 0,
            "Vowel_Swap_count": 0,
            "Wrong_TLD_count": 0,
            "Omission_count": 0,
            "Repetition_count": 0,
            "Transposition_count": 0,
            "Hyphenation_count": 0,
            "Various_count": 0,
            "Missing_Dot_count": 0,
            "Homophones_count": 0,
            "Common_Misspelling_count": 0,
            "Strip_Dashes_count": 0,
            "Homoglyph": list(),
            "Insertion": list(),
            "Bitsquatting": list(),
            "Subdomain": list(),
            "Addition": list(),
            "Replacement": list(),
            "Vowel_Swap": list(),
            "Wrong_TLD": list(),
            "Omission": list(),
            "Repetition": list(),
            "Transposition": list(),
            "Hyphenation": list(),
            "Various": list(),
            "Missing_Dot": list(),
            "Homophones": list(),
            "Common_Misspelling": list(),
            "Strip_Dashes": list()
    }
    for choice in choices:
        temp = choice.split(' ')
        if domain == temp[2]:
            detail[domain]["domain_count"]+=1
            detail[domain][temp[0]+"_count"]+=1
            detail[domain][temp[0]].append(temp[1])
print_count = 0
for domain in domains:
    for fuzzer_name in fuzzer_names:
        #In case <=10 , get it all.
        if detail[domain][fuzzer_name+"_count"] <= 10 and detail[domain][fuzzer_name+"_count"] >0:
            for printme in detail[domain][fuzzer_name]:
                print printme
                print_count+=1
        #In case >10 random it just 10,
        elif detail[domain][fuzzer_name+"_count"] != 0:
            list_of_random_items = random.sample(detail[domain][fuzzer_name],10)  
            i = 0
            while i < 10:
                print detail[domain][fuzzer_name][i]
                i+=1
            print_count+=10
