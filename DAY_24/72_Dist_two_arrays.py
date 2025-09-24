'''Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1'''






# My logic using loop and condition

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        ans = 0
        for x in arr1:
            valid = True
            for y in arr2:
                if abs(x - y) <= d:
                    valid = False
                    break
            if valid:
                ans += 1
        return ans
    





# Leetcode optimal solution


# Some remarks on how to interpret this algorithm.
#
# Each branch of the nested if-else statement will lead you to a single conclusion about your
# current configuration of pointers regarding two questions:
# 1. does the i-th element of arr1 sastisfies distance condition or not -- if not we drop i-th
# element, i.e. ignore augmenting distance counter and advance the pointer
# 2. is the j-th element of arr2 neccessary for comparisons with current or next elements of
# arr1 -- if not we advance the j pointer
#
# The concluding correction accounts for the tail of arr1 in the case when its values are greater
# than all of the arr2. I need it because my algorithm for the sake of simplicity and its
# correctness assumes that there will be always a concluding element of arr2 that is greater
# that any elmeent of arr1. You can see on the test sets it is not always the case, therefore is
# the correction.


class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        dist = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1
            else:
                if arr2[j] - arr1[i] > d:
                    i += 1
                    dist += 1
                else:
                    i += 1
        dist += len(arr1) - i
        return dist