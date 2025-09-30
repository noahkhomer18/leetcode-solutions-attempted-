# 011 - Container With Most Water

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Greedy

## Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice that you may not slant the container.**

## Examples

### Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
```

### Example 2:
```
Input: height = [1,1]
Output: 1
```

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Approach

**Two Pointers Technique:**
- Start with two pointers at the beginning and end of the array
- Calculate the area between the two lines
- Move the pointer pointing to the shorter line inward
- Keep track of the maximum area found

## Time Complexity
- **Time:** O(n) - single pass through the array
- **Space:** O(1) - only using two pointers

## Key Insights
- The area is limited by the shorter of the two lines
- Moving the pointer at the taller line won't increase the area
- Moving the pointer at the shorter line might find a better area
