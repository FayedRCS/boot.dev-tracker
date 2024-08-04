def merge(dict1, dict2):
    
    dict3 = {}

    for dict in dict1:
        dict3[dict] = dict1[dict]

    for dict in dict2:
        dict3[dict] = dict2[dict]
    
    return dict3

def total_score(score_dict):

    each_score = 0
    
    for score in score_dict:

        if score_dict[score] >= 0:
            each_score += score_dict[score]
        
    if each_score == 0:
        return 0
    
    return each_score




dictionary_test_1 = {
    "car" : 12,
    "model" : 2017
}

dictionary_test_2 = {
    "skibidi" : "toilet",
    "Ohio" : "rizz"
}

print(merge(dictionary_test_1, dictionary_test_2))

print(total_score(merge(dictionary_test_1, dictionary_test_2)))