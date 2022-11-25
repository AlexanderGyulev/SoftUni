course = ""
students_dictionary = {}
while True:
    command = input().split(":")
    if len(command) < 3:
        course = command
        break
    name, student_id, student_course = command[0], command[1], command[2]
    if student_course not in students_dictionary.keys():
        students_dictionary[student_course] = []
    students_dictionary[student_course].append(f"{name} - {student_id}")

searched_course = command[0].replace("_", " ")
for student in students_dictionary[searched_course]:
    print(student)
