# Longest Palindromic Substring

**Problem Number:** 5  
**Difficulty:** Medium  
**LeetCode Link:** https://leetcode.com/problems/longest-palindromic-substring/

## Problem Description

Given a string `s`, return the longest palindromic substring in `s`.

## Examples

### Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

### Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

## Constraints

- 1 <= s.length <= 1000
- s consist of only digits and English letters.

## Solutions

See the `solutions/` folder for my attempted solutions.

## Notes

- [x] First attempt - Expand Around Centers approach
- [x] Optimized solution - O(n²) time complexity, O(1) space
- [x] Edge cases handled - Single character, all same characters, even/odd length palindromes
