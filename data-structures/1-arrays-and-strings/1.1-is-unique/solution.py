def is_unique(str):
    chars = {}

    for char in str:
        if char in chars:
            return False
        else:
            chars[char] = 1  # one occurence of the character

    return True


print(is_unique("abc"))  # True
print(is_unique("aab"))  # False
print(is_unique("Kevin Bacon"))  # False
print(is_unique("Tenchi Muyo"))  # True
