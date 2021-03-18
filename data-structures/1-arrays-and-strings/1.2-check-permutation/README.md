# 1.2 Check Permutation

Given two strings, write a method to decide if one is a permutation of the other.

## Approach

Similar to [1.1](https://github.com/fahali/ctci/tree/main/data-structures/1-arrays-and-strings/1.1-is-unique), we can create a character map and record their occurences by iterating over the first string. Then, we iterate over the second string and decrement occurences. If the occurences becomes 0, remove that key from the map. If we try to decrement a key's value where the key does not exist, then we don't have a permutation. Likewise, if we finish iterating over the second string and the map still has keys, then we don't have a permutation. If we end up with an empty map, the strings are permutations.

This approach is **O(n) in time complexity**, because we loop twice, so our complexity is reduced from O(2n) to O(n), and **O(1) in space complexity**, for similar reasons to [1.1](https://github.com/fahali/ctci/tree/main/data-structures/1-arrays-and-strings/1.1-is-unique): there is an upper limit to the number of keys we need to store in our map.

-   ASCII: 128
-   extended ASCII: 256
-   Unicode: 140,000+
