def average_grade(student, grades):
    
    for i in range(len(student)):
        print(f"Student: {student[i]}; grade: {grades[i]}")

    total_score = 0

    for grade in grades:
        total_score += grade

    grade_average = total_score / len(grades)

    return print(f"Class grade average: {grade_average}")


test1 = ["Alice", "Bob", "Charlie", "David", "Eve"]
test2 = [85, 92, 78, 90, 88]

average_grade(test1, test2)