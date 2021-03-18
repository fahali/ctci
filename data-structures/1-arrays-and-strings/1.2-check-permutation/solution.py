def check_permutation(str1, str2):
    # different sized strings cannot be permutations
    if len(str1) != len(str2):
        return False

    chars = {}
    for char in str1:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for char in str2:
        if char in chars:
            chars[char] -= 1
            if chars[char] == 0:
                del chars[char]
        else:
            return False

    if len(chars) == 0:
        return True
    else:
        return False


print(check_permutation("racecar", "carrace"))  # True
print(check_permutation("abc", "abcd"))  # False
print(check_permutation("aaabc", "aabcb"))  # False
print(check_permutation("abcdef", "abcdefg"))  # False
