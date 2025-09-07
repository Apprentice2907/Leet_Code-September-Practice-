'''Suppose we have a class:
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:
We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

Example 1:

Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.'''






# My logic

class Foo(object):
    def __init__(self):
        self.done = []

    def first(self, printFirst):
        printFirst()
        self.done.append("first")

    def second(self, printSecond):
        while True:
            if "first" in self.done:
                printSecond()
                self.done.append("second")
                break

    def third(self, printThird):
        while True:
            if "second" in self.done:
                printThird()
                self.done.append("third")
                break








# Leet code best solution

from threading import Lock
class Foo(object):
    def __init__(self):
        self.firstJob = Lock()
        self.secondJob = Lock()
        self.firstJob.acquire()
        self.secondJob.acquire()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJob.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        with self.firstJob:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.secondJob.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        with self.secondJob:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
