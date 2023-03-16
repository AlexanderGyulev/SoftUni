from collections import deque

working_bees = deque(map(int, input().split()))
nectar_values = deque(map(int, input().split()))
sequence_of_symbols = deque(input().split())

total_honey = 0

while working_bees and nectar_values:
    bee = working_bees.popleft()
    nectar = nectar_values.pop()
    curr_symbol = sequence_of_symbols.popleft()
    if bee > nectar:
        working_bees.appendleft(bee)
        sequence_of_symbols.appendleft(curr_symbol)
    elif bee < nectar:
        if curr_symbol == "+":
            x = abs(bee + nectar)
        elif curr_symbol == "-":
            x = abs(bee - nectar)
        elif curr_symbol == "*":
            x = abs(bee * nectar)
        else:
            x = abs(bee / nectar)
        total_honey += x

print(f"Total honey made: {total_honey}")

if len(working_bees):
    print(f"Bees left: {', '.join(str(el) for el in working_bees)}")
if len(nectar_values):
    print(f"Nectar left: {', '.join(str(el) for el in nectar_values)}")
