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
        _ = self.peek()
        return self.t.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.t:
            while self.s:
                self.t.append(self.s.pop())
        return self.t[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.s and not self.t


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
param_5 = obj.peek()
print(param_2, param_3, param_4, param_5)
