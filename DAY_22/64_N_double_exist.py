'''Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 '''







# My logic but not optimal using simple looping

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            for j in range(len(arr)):
                if(i!=j and arr[i]==2*arr[j]):
                    return True
        return False
    





# Optimal solution for this problem
# making the set and then checking the conditions backward like num*2 and num%2 

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen=set()
        for num in arr:
            if num*2 in seen or (num%2==0 and num//2 in seen):
                return True
            seen.add(num)
        return False

        