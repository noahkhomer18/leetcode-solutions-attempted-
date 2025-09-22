class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return x == reversed_num or x == reversed_num // 10

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))   # True
    print(s.isPalindrome(-121))  # False
    print(s.isPalindrome(10))    # False
    print(s.isPalindrome(0))     # True
