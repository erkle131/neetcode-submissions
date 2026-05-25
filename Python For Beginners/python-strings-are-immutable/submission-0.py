def remove_fourth_character(word: str) -> str:
    new_word = word[:3] + word[4:]
    return new_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
