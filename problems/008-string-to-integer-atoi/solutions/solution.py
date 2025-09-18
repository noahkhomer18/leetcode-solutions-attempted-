class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, n = 0, len(s)
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Determine sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: Convert digits with overflow detection
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow before adding the digit
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        return sign * num

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: s = "42"
    result1 = solution.myAtoi("42")
    print(f"Example 1: {result1}")  # Expected: 42
    
    # Example 2: s = "   -042"
    result2 = solution.myAtoi("   -042")
    print(f"Example 2: {result2}")  # Expected: -42
    
    # Example 3: s = "1337c0d3"
    result3 = solution.myAtoi("1337c0d3")
    print(f"Example 3: {result3}")  # Expected: 1337
    
    # Example 4: s = "0-1"
    result4 = solution.myAtoi("0-1")
    print(f"Example 4: {result4}")  # Expected: 0
    
    # Example 5: s = "words and 987"
    result5 = solution.myAtoi("words and 987")
    print(f"Example 5: {result5}")  # Expected: 0
    
    # Additional test cases
    result6 = solution.myAtoi("   +123")
    print(f"Positive with spaces: {result6}")  # Expected: 123
    
    result7 = solution.myAtoi("2147483648")
    print(f"Overflow case: {result7}")  # Expected: 2147483647 (INT_MAX)
    
    result8 = solution.myAtoi("-2147483649")
    print(f"Underflow case: {result8}")  # Expected: -2147483648 (INT_MIN)
