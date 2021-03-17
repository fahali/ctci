def isUnique(str):
    chars = {}

    for char in str:
        if char in chars:
            return False
        else:
            chars[char] = 1  # one occurence of the character

    return True


print(isUnique("abc"))  # True
print(isUnique("aab"))  # False
print(isUnique("Kevin Bacon"))  # False
print(isUnique("Tenchi Muyo"))  # True
