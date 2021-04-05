# 1.6 String Compression

Implement a method to perform basic string compression using the counts of repeated characters. For example the string `aabcccccaaa` would become `a2b1c5a3`. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters.

## Approach

In Python, strings can be "indexed" into like arrays, where each index is one character. We can use a `for` loop to iterate over each "index" of the array, i.e., every character in the string. We start by recording the current character and we increment the occurence `count` by 1. If we are at the end of the string `or` the next consecutive character is different from the current one, we should append to our `result` string the current character and the `count`. Then reset the `count` for the next unique character. At the end, compare the lengths of both and return the string that is shorter as per the problem statement.

That is a good way to do it, but string concatenation in Python can give us `O(n^2)` performance in the worst case. A better way to do it is to build a list of sequences: what I am calling a character and its occurence count. At the end, join the list to an empty string to avoid potential performance bottlenecks. The final solution takes `O(n)` time as we still need to iterate over every character. The space complexity is more tricky to determine, as the spread of characters determines how big the result gets. I will hazard a guess and say it is `O(n)` amortized.
