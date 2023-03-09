number_of_students = int(input())

students_dictionary = {}

for _ in range(number_of_students):
    name, grade = input().split(" ")
    if name not in students_dictionary:
        students_dictionary[name] = []
    students_dictionary[name].append(float(grade))

for keys, values in students_dictionary.items():
    average = sum(values) / len(values)
    current_values = ""
    for elements in values:
        current_values += f"{elements:.2f}" + " "
    print(f"{keys} -> {current_values}(avg: {average:.2f})")
