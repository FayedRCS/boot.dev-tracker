def get_test_score(answer_sheet, student_answers):

    #making sure the lists are the same size
    if len(answer_sheet) != len(student_answers):
        return "error sheets are not the same"
    
    #has to be outside the list so it doest reset... learned hte hard way
    correct = 0
    wrong = 0

    #we only need one loop, because we know the answers are at the same indexes and can compare them
    
    for i in range(len(student_answers)):
            
            if student_answers[i] == answer_sheet[i]:
                correct += 1
            else:
                wrong += 1

    percentage = (correct / (wrong +correct)) * 100

    return float(percentage)
    
    

answer_sheet = ["A", "A", "C", "D", "D", "B", "C", "D",]
student_sheet = ["A", "B", "C", "A", "D", "B", "C", "D"]

# Print the return value of the function
print(get_test_score(answer_sheet, student_sheet))