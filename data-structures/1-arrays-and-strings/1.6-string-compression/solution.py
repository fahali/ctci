def string_compression(str):
    og_len = len(str)

    counts = []
    occurs = 0

    for i in range(og_len):
        char = str[i]
        occurs += 1

        # check that we aren't at the end of the string first
        # so we have valid index to check for our second condition
        if i + 1 >= og_len or char != str[i + 1]:
            counts.append(f"{char}{occurs}")
            occurs = 0

    result = "".join(counts)
    if len(result) < og_len:
        return result
    else:
        return str


print(string_compression("aabcccccaaa"))  # a2b1c5a3
print(string_compression("a"))  # a
print(string_compression("aa"))  # aa
print(string_compression("aaa"))  # a3
print(string_compression("aaab"))  # aaab
print(string_compression("aabb"))  # aabb
print(string_compression("aaabb"))  # a3b2
