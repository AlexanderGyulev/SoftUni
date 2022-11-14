def happiness_checker(sequence, factor):
    happiness_list = list(map(lambda x: int(x) * factor, sequence))
    average = sum(happiness_list) / len(happiness_list)
    happiness_above_average = list(lambda x: x for x in happiness_list if x >= average)
    if len(happiness_above_average) >= average:
        return f"Score: {len(happiness_above_average)}/{len(happiness_list)}. Employees are happy!"
    else:
        return f"Score: {len(happiness_above_average)}/{len(happiness_list)}. Employees are not happy!"


employee_happiness = input().split(" ")
happiness_factor = int(input())
result = happiness_checker(employee_happiness, happiness_factor)
print(result)
