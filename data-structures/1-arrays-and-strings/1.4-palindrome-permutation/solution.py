def palindrome_permutation(str):
    if len(str) <= 1:
        return True

    lowered = str.lower()
    odds = 0
    map = {}

    for char in lowered:
        if char == " ":
            continue

        if char in map:
            map[char] += 1

            if map[char] % 2 == 0:
                odds -= 1
            else:
                odds += 1
        else:
            map[char] = 1
            odds += 1

    return odds <= 1


print(palindrome_permutation("Tact Coa"))  # True
print(palindrome_permutation("RACecar"))  # True
print(palindrome_permutation("palindrome"))  # False
print(palindrome_permutation(""))  # True
print(palindrome_permutation("a"))  # True
print(palindrome_permutation("ab"))  # False
