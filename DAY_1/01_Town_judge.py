'''In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1'''





# My logc but failed 

class Solution(object):
    def findJudge(self, n, trust):
        judge = None
        flag = True

        for a, b in trust:
            if not (1 <= a <= n and 1 <= b <= n):
                return -1
            if judge is None:
                judge = b
            else:
                if judge != b:
                    flag = False
            if a == judge:
                return -1

        if not flag or judge is None:
            return -1

        town = set([a for a, b in trust if b == judge])
        if len(town) == n - 1:
            return judge
        return -1






# So i used chatGPT and heres the logic 

class Solution(object):
    def findJudge(self, n, trust):
        town = set()
        judge = {i: set() for i in range(1, n + 1)}

        for a, b in trust:
            town.add(a)
            judge[b].add(a)

        for person in range(1, n + 1):
            if person in town:
                continue
            if len(judge[person]) == n - 1:
                return person

        return -1







# Leet code best solution

class Solution(object):
    def findJudge(self, n, trust):
        n=n+1
        trusted=[0]*n
        trusts=[False]*n
        for u,v in trust:
            trusted[v]+=1
            trusts[u]=True
        #print(trusts)
        #print(trusted)
        for i in range(1,n):
            if trusted[i]==n-2 and not trusts[i]:
                return i
        return -1