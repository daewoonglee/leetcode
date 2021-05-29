class MinStack(object):
    # 0.025315284729003906
    # def __init__(self):
    #     self.stack = []
    #
    # def push(self, val):
    #     self.stack.append(val)
    #
    # def pop(self):
    #     self.stack.pop()
    #
    # def top(self):
    #     return self.stack[-1]
    #
    # def getMin(self):
    #     return min(self.stack)

    # code refactoring - 0.03282785415649414
    # def __init__(self):
    #     self.stack = []
    #     self.min_nums = []
    #
    # def push(self, val):
    #     self.stack.append(val)
    #     if not self.min_nums or self.min_nums[-1] > val:
    #         self.min_nums.append(val)
    #     else:
    #         self.min_nums.append(self.min_nums[-1])
    #
    # def pop(self):
    #     self.stack.pop()
    #     self.min_nums.pop()
    #
    # def top(self):
    #     return self.stack[-1]
    #
    # def getMin(self):
    #     return self.min_nums[-1]

    # code refactoring (R) - 0.02877187728881836
    def __init__(self):
        self.stack = []

    def push(self, val):
        if self.stack:
            self.stack.append([val, min(val, self.stack[-1][1])])
        else:
            self.stack.append([val, val])

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


# ["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]]
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())

if __name__ == '__main__':
    import time
    start = time.time()
    for _ in range(10000):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        obj.getMin()
        obj.pop()
        obj.top()
        obj.getMin()
        del obj
    print(f"running time: {time.time() - start}")
