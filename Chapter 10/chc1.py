def get_english_grade(student):

    #cascading through the nested dictionary... returns the value of the outer most key
        
    return student["type"]["student"]["courses"]["English_1010"]["current_grade"]