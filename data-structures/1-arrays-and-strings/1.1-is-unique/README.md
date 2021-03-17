# 1.1 Is Unique

Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

## Approach

We can iterate over the string and keep a map of each character we've encountered. If the current character does not exist in the map, add it to the map for future reference. Otherwise, we don't have all unique characters. This results in **O(n) time complexity**, because we might have to check every character in the string, and **O(1) space complexity**, because space is dependent on the character encoding: ASCII accounts for 128 possible values, extended ASCII accounts for 256 possible values, and Unicode accounts for 140,000+ values. We can't form a string with all unique characters if our map grows to be bigger than these sizes, so encountering strings greater than these sizes automatically disqualifies them.

## No additional structures

Sort the string and check consecutive characters: if you have a match you don't have all unique characters. I searched for an efficient, in place sorting algorithm, but came up short. The best trade off seems to be **Quicksort**, which has a space complexity of **[O(log n)](https://en.wikipedia.org/wiki/Quicksort#Space_complexity)**, if the implementation is [tail call optimized](https://en.wikipedia.org/wiki/Tail_call). Of course, Quicksort has a worst case time complexity of **O(n<sup>2</sup>)**, but the average, real world use case tends to be **O(n log n)**.
