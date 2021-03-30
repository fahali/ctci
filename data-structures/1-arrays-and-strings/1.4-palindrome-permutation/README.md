# 1.4 Palindrome Permutation

Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a re-arrangement of letters. The permutation does not need to be limited to just dictionary words.

EXAMPLE

Input: `Tact Coa`

Output: `true` (`tacocat`, `atco cta`, etc)

## Approach

We can observe two things right away from the example provided:

1. case does not matter
2. space characters are not important

Let's determine what makes a palindrome. A palindrome will have a "middle" where the sequence going forwards is mirrored exactly in the same order from that point. The string can have at most one character that has an odd number of occurences; all other characters in the string must have an even number of occurences. This way, they can be evenly distributed on both sides of the "mirror" point, and the singular character can exist at this mirror point.

An `O(n)` approach is to use a hashmap where the keys are the characters and the values are occurences of the character. Then, we can iterate again over the hashmap to check if there is only one character with an odd number of occurences. Since we are only dealing with characters that can form words or phrases, it is safe to say we are dealing with the Latin alphabet, so we can say that this approach will take constant space `O(1)`: we only need to store the keys for 26 characters and their values are integers, which are trivial to store.

A second optimized approach (gotten from the book) is to keep count of all characters that have an odd number of occurences as we iterate through the string the first time. If at the end of the iteration we find that our count is greater than 1, it is impossible to have a palindrome (by our definition above).
