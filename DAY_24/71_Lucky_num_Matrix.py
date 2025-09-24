'''Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.'''








# My logic using loop and condition

class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for i in range(len(matrix)):
            rowm = min(matrix[i])
            coli = matrix[i].index(rowm)
            colm = max(matrix[r][coli] for r in range(len(matrix)))
            if rowm == colm:
                res.append(rowm)
        return res
    



# Leetcode optimal solution

class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for i in range(len(matrix)):
            row_min = min(matrix[i])
            col_index = matrix[i].index(row_min)
            
            if all(row[col_index] <= row_min for row in matrix):
                res.append(row_min)
        
        return res