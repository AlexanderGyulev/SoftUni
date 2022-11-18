number_of_snowballs = int(input())

best_snowball_value = 0
best_snowball_weight = 0
best_time_to_target = 0
best_snowball_quality = 0

for snowballs in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_to_target = int(input())
    snowball_quality = int(input())
    snowball_value = (weight_of_snowball / time_to_target) ** snowball_quality
    if snowball_value > best_snowball_value:
        best_snowball_value = int(snowball_value)
        best_snowball_weight = weight_of_snowball
        best_time_to_target = time_to_target
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_time_to_target} = {best_snowball_value} ({best_snowball_quality})")
