'''You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

 

Example 1:

Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: nums = [1,1,1]
Output: [false,false,false]'''






# My logic using conversion into string and then substring and then checking

class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        result = []
        s = ""
        for bit in nums:
            s += str(bit)                  
            number = int(s, 2)             
            if number % 5 == 0:            
                result.append(True)
            else:
                result.append(False)
        return result
    






# Leet code best solution

class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        result = []
        curr = 0
        
        for bit in nums:
            # shift left and add the new bit
            curr = (curr * 2 + bit) % 5  
            result.append(curr == 0)
        
        return result


        