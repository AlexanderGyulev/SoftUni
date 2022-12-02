link_input = input().split("\\")

last_part = link_input[-1].split(".")
file_name = last_part[0]
extension = last_part[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")