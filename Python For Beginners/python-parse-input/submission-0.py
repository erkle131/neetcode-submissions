from typing import List

def read_integers() -> List[int]:
    number_string = input()
    string_list = number_string.split(",")
    int_list = [int(string) for string in string_list]
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
