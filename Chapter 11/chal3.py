def find_missing_ids(first_ids, second_ids):

    our_set = set()
    final_list = []
    
    for i in first_ids:

        if i not in second_ids:

            our_set.add(i)

    for j in our_set:
        final_list.append(j)
    
    return final_list

        


