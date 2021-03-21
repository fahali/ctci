# 1.3 URLify

Write a method to replace all spaces in a string with `"%20"`. You may assume the string has sufficient space at the end to hold the additional characters, and you are given the "true" length of the string.

```
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
```

## Approach

Iterate over the string, one character at a time, with a step counter. Build a result string, by appending the current character to the result string. When a space character `" "` is encountered, append `"%20"` instead of the space. After every iteration, increment the step counter. Stop iterating once we have reached the "true" length of the string provided as input. Return the result.

This approach is **O(n)** in time complexity where **n** is the "true" length of the string, and **O(n)** in space complexity, because we need extra space equal to the "true" length of the string.
