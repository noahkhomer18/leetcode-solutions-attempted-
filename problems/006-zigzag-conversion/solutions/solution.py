class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        index, step = 0, 1
        
        for char in s:
            rows[index] += char
            
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
                
            index += step
            
        return ''.join(rows)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: s = "PAYPALISHIRING", numRows = 3
    result1 = solution.convert("PAYPALISHIRING", 3)
    print(f"Example 1: {result1}")  # Expected: "PAHNAPLSIIGYIR"
    
    # Example 2: s = "PAYPALISHIRING", numRows = 4
    result2 = solution.convert("PAYPALISHIRING", 4)
    print(f"Example 2: {result2}")  # Expected: "PINALSIGYAHRPI"
    
    # Example 3: s = "A", numRows = 1
    result3 = solution.convert("A", 1)
    print(f"Example 3: {result3}")  # Expected: "A"
    
    # Additional test cases
    result4 = solution.convert("AB", 1)
    print(f"Single row: {result4}")  # Expected: "AB"
    
    result5 = solution.convert("ABC", 2)
    print(f"Two rows: {result5}")  # Expected: "ACB"
