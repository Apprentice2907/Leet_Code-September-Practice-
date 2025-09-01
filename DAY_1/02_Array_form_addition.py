'''The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021'''










# My logic using classic mathematical approach 

class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        kdig= list(map(int, str(k)))
        i,j= len(num)-1, len(kdig)-1
        carry =0
        result=[]

        while i>=0 or j>=0 or carry:
            x= num[i] if i>=0 else 0 
            y = kdig[j] if j >=0 else 0 

            total = x+y+carry
            carry = total//10
            result.insert(0,total % 10)
            i=i-1
            j=j-1
        return result
    





# Second approach using string operation

class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        numl = int("".join(map(str, num)))
        total = numl + k
        return list(map(int, str(total)))









# Leet code best solution

class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        c=k
        i=len(num)-1
        while c:
            if i>=0:
                c+=num[i]
                num[i]=c%10
                c//=10
                i-=1
            else:
                num.insert(0,c%10)
                c//=10
        return num
            