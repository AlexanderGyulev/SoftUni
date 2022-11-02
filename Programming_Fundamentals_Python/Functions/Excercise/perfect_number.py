def perfect_checker(num):
    sum_of_numbers = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_numbers += i
    if sum_of_numbers == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


input_number = int(input())
print(perfect_checker(input_number))
