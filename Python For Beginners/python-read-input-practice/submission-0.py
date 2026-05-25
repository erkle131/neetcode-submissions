def add_two_numbers() -> int:
    line = input()
    strings = line.split(",")
    
    my_sum = 0
    for num in strings:
        my_sum += int(num)
    return my_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
