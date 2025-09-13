'''Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:

Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]'''










# My logic using simple maths and also leetcode best solution

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n= len(grid[0])
        size = m * n

        flat = []
        for i in range(m):
            for j in range(n):
                flat.append(grid[i][j])

        new_flat = [0] * size
        for i in range(size):
            new_index = (i + k) % size
            new_flat[new_index] = flat[i]

        result = []
        idx = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(new_flat[idx])
                idx += 1
            result.append(row)

        return result




# Leet code best solution

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Get the dimensions of the grid.
        m, n = len(grid), len(grid[0])
    
    # Total number of elements.
        total = m * n
    # Effective shifts needed (in case k > total).
        k %= total
    
    # Flatten the grid into a 1D list.
        flat = [num for row in grid for num in row]
    
    # Perform the shift on the flattened list.
    # The last k elements move to the front.
        flat = flat[-k:] + flat[:-k]
    
    # Reconstruct the 2D grid from the shifted list.
        new_grid = []
        for i in range(m):
            new_grid.append(flat[i*n:(i+1)*n])
    
        return new_grid