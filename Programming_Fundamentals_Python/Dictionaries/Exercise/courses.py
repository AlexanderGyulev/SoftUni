courses_dictionary = {}
while True:
    command = input()
    if command == "end":
        break
    command = command.split(" : ")
    course_name = command[0]
    student_name = command[1]
    current_list = [student_name]
    if course_name not in courses_dictionary.keys():
        courses_dictionary[course_name] = list()
    courses_dictionary[course_name].extend(current_list)

for items in courses_dictionary:
    print(f"{items}: {len(courses_dictionary[items])}")
    for elements in courses_dictionary[items]:
        print(f"-- {elements}")
