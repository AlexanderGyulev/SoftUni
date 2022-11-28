company_dictionary = {}

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split(" -> ")
    organization = current_command[0]
    employee_id = current_command[1]
    if organization not in company_dictionary:
        company_dictionary[organization] = list()
    if employee_id not in company_dictionary[organization]:
        company_dictionary[organization].append(employee_id)

for keys in company_dictionary.keys():
    print(keys)
    for identifications in company_dictionary[keys]:
        print(f"-- {identifications}")
