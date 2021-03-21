# 1.3 URLify

Write a method to replace all spaces in a string with `'%20'`. You may assume the string had sufficient space at the end to hold the additional characters, and you are given the "true" length of the string.

```
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
```

## Approach

Iterate over the string, one character at a time. Replace spaces with `'%20'`. If there was a replacement, step over 3 characters instead of 1, to account for the additional characters. Stop when we've traversed the original 13 characters.
