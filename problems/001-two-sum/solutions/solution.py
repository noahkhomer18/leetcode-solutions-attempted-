class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, num in enumerate(nums):
            
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: nums = [2,7,11,15], target = 9
    result1 = solution.twoSum([2,7,11,15], 9)
    print(f"Example 1: {result1}")  # Expected: [0,1]
    
    # Example 2: nums = [3,2,4], target = 6
    result2 = solution.twoSum([3,2,4], 6)
    print(f"Example 2: {result2}")  # Expected: [1,2]
    
    # Example 3: nums = [3,3], target = 6
    result3 = solution.twoSum([3,3], 6)
    print(f"Example 3: {result3}")  # Expected: [0,1]
