def one_replacement(s1, s2):
    diff = False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if diff:
                return False  # no more than one difference

            diff = True

    return True


# s2 is the longer string, determined in the driver function below
def one_insertion(s1, s2):
    idx1 = 0
    idx2 = 0

    while idx1 < len(s1) and idx2 < len(s2):
        if s1[idx1] != s2[idx2]:
            if idx1 != idx2:
                # if we already have different indices and
                # the characters don't match, this can't be one edit away
                return False

            idx2 += 1  # increment the index of the longer string only

        else:
            idx1 += 1
            idx2 += 1

    return True


def one_away(s1, s2):
    # at most string lengths can differ by 1
    s1len = len(s1)
    s2len = len(s2)

    if abs(s1len - s2len) > 1:
        return False

    if s1len == s2len:
        return one_replacement(s1, s2)

    # determine the shorter and longer string
    if s1len + 1 == s2len:
        return one_insertion(s1, s2)
    if s1len - 1 == s2len:
        return one_insertion(s2, s1)

    # falls outside the conditions of one edit away
    return False


print(one_away("pale", "ple"))  # True
print(one_away("pales", "pale"))  # True
print(one_away("pale", "bale"))  # True
print(one_away("pale", "bake"))  # False
