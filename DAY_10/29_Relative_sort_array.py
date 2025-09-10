'''Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]'''






# My logic using enumeration method

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        order = {}
        for i, val in enumerate(arr2):
            order[val] = i

        def sort_key(x):
            return (order.get(x, len(arr2)), x)

        arr1.sort(key=sort_key)
        return arr1
    



# Another easy logic 

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []
        for val in arr2:
            for num in arr1:
                if num == val:
                    result.append(num)
        remaining = []
        for num in arr1:
            if num not in arr2:
                remaining.append(num)

        remaining.sort()
        result.extend(remaining)

        return result
    






# My logic using stack data type

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr1.sort()
        result = []
        for val in arr2:
            stack = []
            while arr1:
                num = arr1.pop(0)
                if num == val:
                    result.append(num)
                else:
                    stack.append(num)
            arr1 = stack
        while arr1:
            result.append(arr1.pop(0))
        return result
    





# Leet code best solution

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        rank = {num: i for i ,num in enumerate(arr2)}
        return sorted(arr1,key=lambda x:(rank.get(x,len(arr2)), x))
        