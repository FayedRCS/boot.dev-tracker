def get_test_score(answer_sheet, student_answers):


    #since we know first index is the name, we just set it as the student_name
    student_name = student_answers[0]
    
    #we slice the rest of the list into a new list called "student sheet", containing the students answers
    student_sheet = student_answers[1:]
    

    #same as chapter challenge 3, making sure the lists are the same lenghts too
    correct = 0
    incorrect = 0

    if len(answer_sheet) != len(student_sheet):
        return "Oopsie, sheets are not compatible"
    
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == student_sheet[i]:
            correct += 1
        else:
            incorrect += 1

    percentage = (correct / (correct + incorrect)) * 100

    return student_name, float(percentage)

test1 = ["1", "2"]
test2 = ["pete", "1", "2"]

print(get_test_score(test1, test2))
