'''Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"'''






# My logic using for loop adn condition

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = ""
        for ch in address:
            if ch == ".":
                result += "[.]"
            else:
                result += ch
        return result
    






# Leet code best solution

class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".","[.]")


        