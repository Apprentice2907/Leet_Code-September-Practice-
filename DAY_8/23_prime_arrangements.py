'''Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)
Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015'''







# ChatGPT logic 

class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        prime_count = 0
        for i in range(1, n + 1):
            if is_prime(i):
                prime_count += 1

        non_prime_count = n - prime_count

        def factorial(x):
            result = 1
            for i in range(1, x + 1):
                result = (result * i) % MOD
            return result

        return (factorial(prime_count) * factorial(non_prime_count)) % MOD
    






# Leet code best solution

class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        def countPrimes(n):
            count = 0
            for i in range(2,n+1):
                flag = 0
                for j in range(2,i//2+1):
                    if (i%j==0):
                        flag = 1
                        break
                if flag == 0:
                    count+=1
            return count
        def fact(n):
            ans = 1
            for i in range(2,n+1):
                ans*=i
            return ans
        
        return ((fact(countPrimes(n))*fact(n-countPrimes(n)))%(7+10**9))