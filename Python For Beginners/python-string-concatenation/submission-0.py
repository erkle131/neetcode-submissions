def concatenate(s1: str, s2: str) -> str:
    new_string = s1 + s2
    if len(new_string) > 10:
        return "Too long!"
    else:
        return new_string




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
