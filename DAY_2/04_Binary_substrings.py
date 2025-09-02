'''Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 '''







# Logic using Group Counting

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        group=[]
        i=0
        n = len(s)
    
        while i < n:
            count = 1
            while i + 1 < n and s[i] == s[i + 1]:
                count += 1
                i += 1
            group.append(count)
            i += 1

        result = 0
        for j in range(len(group) - 1):
            result += min(group[j], group[j + 1])
        
        return result
    




# my Logic using substring and then counting 

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        result = 0

        for i in range(n):
            c0 = 0
            c1 = 0
            pchar = ''
            for j in range(i, n):
                if s[j] == '0':
                    if pchar == '1' and c0 > 0:
                        break  
                    c0 += 1
                else:  
                    if pchar == '0' and c1 > 0:
                        break 
                    c1 += 1
                
                pchar = s[j]
                
                if c0 == c1 and c0 != 0:
                    result += 1

        return result
    





# Leet code best solution

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_count = 0
        current_count = 1
        total_count = 0
        prev_char = s[0]
        for c in s[1:]:
            if c == prev_char:
                current_count += 1
            else:
                total_count += min(prev_count, current_count)
                prev_count = current_count
                current_count = 1
            prev_char = c
    
        total_count += min(prev_count, current_count)

        return total_count

        