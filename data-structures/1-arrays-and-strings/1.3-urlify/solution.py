def URLify(str, trueLen):
    step = 0
    result = ""
    while step < trueLen:
        cur = str[step]
        if cur == " ":
            result += "%20"
        else:
            result += cur
        step += 1

    return result


print(URLify("Mr John Smith    ", 13))