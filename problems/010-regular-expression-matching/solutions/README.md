# Regular Expression Matching - Solutions

## Solution: Dynamic Programming (2D Table)
**Time Complexity:** O(n·m)  
**Space Complexity:** O(n·m)  
Where `n = len(s)` and `m = len(p)`.

### Approach
Let `dp[i][j]` indicate whether the prefix `s[:i]` matches the pattern `p[:j]`.

Rules:
- If `p[j-1]` is a normal character or `.`, then it matches iff `s[i-1]` equals it (or `.`) and `dp[i-1][j-1]` is true.
- If `p[j-1]` is `*`, it can represent:
  - Zero occurrences of the previous character: `dp[i][j-2]`
  - One or more occurrences: if `p[j-2]` matches `s[i-1]` (or `.`), then `dp[i-1][j]`.

Initialization:
- `dp[0][0] = True`.
- For empty string `s`, handle patterns like `a*`, `a*b*`, etc.: when `p[j-1] == '*'`, set `dp[0][j] = dp[0][j-2]`.

### Code
```python
class Solution(object):
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j]
        return dp[len(s)][len(p)]
```

### Why This Works
- The DP captures all ways `*` can expand while enforcing full-string match.
- Matches the exact semantics required by LeetCode 10.

### Test Results
- ✅ `("aa", "a") → False`
- ✅ `("aa", "a*") → True`
- ✅ `("ab", ".*") → True`
- ✅ `("aab", "c*a*b") → True`
- ✅ `("mississippi", "mis*is*p*.") → False`
