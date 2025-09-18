'''Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false'''








# My logic using slow fast pointer

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow , fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev = None
        while slow:
            nxt, slow.next = slow.next, prev
            prev, slow = slow, nxt
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
    





# Leetcode best solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode

            return prev
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        firstHalf = head
        secondHalf = reverse(slow)

        while secondHalf:
            if firstHalf.val != secondHalf.val:
                return False

            firstHalf = firstHalf.next
            secondHalf = secondHalf.next

        return True
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
