'''Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False'''










# My logic as converted this code into python from c++ code

from Queue import Queue

class MyStack(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        while not self.q1.empty():
            self.q2.put(self.q1.get())

        self.q1.put(x)

        while not self.q2.empty():
            self.q1.put(self.q2.get())

    def pop(self):
        return self.q1.get()

    def top(self):
        return self.q1.queue[0] 

    def empty(self):
        return self.q1.empty()







# different code

class MyStack(object):

    def __init__(self):
        self.stack = []
        self.head = -1

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.head += 1
        

    def pop(self):
        """
        :rtype: int
        """
        r = self.stack.pop(self.head)
        self.head -= 1
        return r
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.head]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()