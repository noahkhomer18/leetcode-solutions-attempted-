# Longest Substring Without Repeating Characters

**Problem Number:** 3  
**Difficulty:** Medium  
**LeetCode Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Problem Description

Given a string `s`, find the length of the longest substring without repeating characters.

## Examples

### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints

- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

## Solutions

See the `solutions/` folder for my attempted solutions.

## Notes

- [x] First attempt - Sliding Window with Hash Map
- [x] Optimized solution - O(n) time complexity
- [x] Edge cases handled - Empty string, single character, all same characters
