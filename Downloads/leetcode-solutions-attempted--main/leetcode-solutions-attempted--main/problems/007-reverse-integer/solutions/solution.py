class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = int(str(x_abs)[::-1]) * sign
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: x = 123
    result1 = solution.reverse(123)
    print(f"Example 1: {result1}")  # Expected: 321
    
    # Example 2: x = -123
    result2 = solution.reverse(-123)
    print(f"Example 2: {result2}")  # Expected: -321
    
    # Example 3: x = 120
    result3 = solution.reverse(120)
    print(f"Example 3: {result3}")  # Expected: 21
    
    # Additional test cases
    result4 = solution.reverse(0)
    print(f"Zero: {result4}")  # Expected: 0
    
    result5 = solution.reverse(1534236469)
    print(f"Overflow case: {result5}")  # Expected: 0
    
    result6 = solution.reverse(-2147483648)
    print(f"Min int: {result6}")  # Expected: 0
