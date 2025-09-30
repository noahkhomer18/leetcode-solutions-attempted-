# Regular Expression Matching

**Problem Number:** 10  
**Difficulty:** Hard  
**LeetCode Link:** https://leetcode.com/problems/regular-expression-matching/

## Problem Description
Implement regular expression matching with support for `.` and `*`.
- `.` Matches any single character.
- `*` Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

## Examples

### Example 1:
```
Input: s = "aa", p = "a"
Output: false
```

### Example 2:
```
Input: s = "aa", p = "a*"
Output: true
```

### Example 3:
```
Input: s = "ab", p = ".*"
Output: true
```

## Constraints
- 1 <= s.length <= 20
- 1 <= p.length <= 30
- `s` contains only lowercase English letters
- `p` contains only lowercase English letters, `.` and `*`
- It is guaranteed for each appearance of `*`, there will be a previous valid character to match

## Solutions
See the `solutions/` folder for my attempted solutions.

## Notes
- [x] DP solution using full table, O(n·m) time and space
- [x] Handles leading `x*` blocks for empty string
- [x] Covers `.` and `*` semantics exactly as LeetCode specifies
