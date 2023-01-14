from collections import deque

queue = deque()

while True:
    current_command = input()
    if current_command == "End":
        break
    if current_command == "Paid":
        for _ in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(current_command)

ppl_left = len(queue)
print(f"{ppl_left} people remaining.")

