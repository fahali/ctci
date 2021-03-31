# 1.5 One Away

There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE

```
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
```

## Approach

It can be assumed that the strings we are checking should be similar in length, at most 1 character length different. If they're not, it's impossible to be one edit away. We can step through both strings in one loop if we make some observations about the question.

In regards to the problem statement, insertion and removal are the same operation: they indicate a character exists in one string and not the other, so we can check for both conditions with the same function. Otherwise, for insertion, removal, and replacement, we need to keep track of how many changes need to be made as we compare characters for both strings. If we already have 1 existing change, and another needs to be made, it's impossible to be one edit away. If we've exited the loop and we only have at most 1 change, then the strings are one edit away.
