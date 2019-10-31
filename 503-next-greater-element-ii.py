"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""
class Solution1:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, stack = len(nums), []
        ans = [-1] * l
        for i in range(2*l-1,-1,-1):
            index = i % l
            while stack and nums[index] >= nums[stack[-1]]:
                stack.pop()
            if stack:
                ans[index] = nums[stack[-1]]
            stack.append(index)
        return ans

# Time Limit Exceeded
class Solution2:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        length = len(nums)
        for i in range(length):
            j = i - length
            k = j + 1
            flag = 0
            while k > j and k < i:
                if nums[k] > nums[i]:
                    l.append(nums[k])
                    flag = 1
                    break
                k += 1
            if flag == 0:
                l.append(-1)
        return l