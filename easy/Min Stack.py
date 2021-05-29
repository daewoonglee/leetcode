class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


# ["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]]
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())

