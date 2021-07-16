class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.top_idx = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.nums.append(x)
        self.top_idx += 1
        return None

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.top_idx:
            self.top_idx -= 1
            return self.nums.pop()
        else:
            return None

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.nums[self.top_idx-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.top_idx


# Your MyStack object will be instantiated and called as such:
obj = MyStack()

# obj.push(1)
# obj.push(2)
# param_2 = obj.top()
# param_3 = obj.pop()
# param_4 = obj.empty()
# print(param_2, param_3, param_4)

# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
obj.push(1)
param_2 = obj.pop()
obj.push(2)
param_3 = obj.top()
print(param_2, param_3)
