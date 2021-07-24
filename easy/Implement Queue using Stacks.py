class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = list()
        self.t = list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.s:
            self.t.append(self.s.pop())
        output = self.t.pop()
        while self.t:
            self.s.append(self.t.pop())
        return output

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.t = self.s[:]
        n = None
        while self.t:
            n = self.t.pop()
        return n

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return False if self.s else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(10)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# print(param_2, param_3, param_4)

obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2, param_3, param_4)
