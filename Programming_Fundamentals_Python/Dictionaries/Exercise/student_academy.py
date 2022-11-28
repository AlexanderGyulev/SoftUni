total_students = int(input())
students_dictionary = {}

for indexes in range(total_students):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_dictionary:
        students_dictionary[student_name] = list()
    students_dictionary[student_name].append(student_grade)

for students in students_dictionary:
    total_score = 0
    total_iterations = 1
    average_score = 0
    for items in students_dictionary[students]:
        total_score += items
        average_score = total_score / total_iterations
        total_iterations += 1
    if average_score >= 4.50:
        print(f"{students} -> {average_score:.2f}")
