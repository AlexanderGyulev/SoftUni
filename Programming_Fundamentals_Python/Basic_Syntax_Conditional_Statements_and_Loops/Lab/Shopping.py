total_budget = int(input())
total_spent = 0

current_command = input()
while current_command != "End":
    current_command = int(current_command)
    total_spent += current_command
    if total_spent > total_budget:
        print("You went in overdraft!")
        break
    current_command = input()
else:
    print("You bought everything needed.")