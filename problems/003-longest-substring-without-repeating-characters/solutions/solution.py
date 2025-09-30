class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        max_len = 0
        start = 0
        for i, c in enumerate(s):
            if c in char_index and char_index[c] >= start:
                start = char_index[c] + 1
            char_index[c] = i
            max_len = max(max_len, i - start + 1)
        return max_len

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: s = "abcabcbb"
    result1 = solution.lengthOfLongestSubstring("abcabcbb")
    print(f"Example 1: {result1}")  # Expected: 3
    
    # Example 2: s = "bbbbb"
    result2 = solution.lengthOfLongestSubstring("bbbbb")
    print(f"Example 2: {result2}")  # Expected: 1
    
    # Example 3: s = "pwwkew"
    result3 = solution.lengthOfLongestSubstring("pwwkew")
    print(f"Example 3: {result3}")  # Expected: 3
    
    # Additional test cases
    result4 = solution.lengthOfLongestSubstring("")
    print(f"Empty string: {result4}")  # Expected: 0
    
    result5 = solution.lengthOfLongestSubstring("a")
    print(f"Single character: {result5}")  # Expected: 1
    
    result6 = solution.lengthOfLongestSubstring("dvdf")
    print(f"Edge case: {result6}")  # Expected: 3
