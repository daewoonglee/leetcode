class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums        
        self.log = dict()

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left in self.log:
            if right in self.log[left]:
                return self.log[left][right]
        else:
            self.log[left] = dict()
        self.log[left][right] = sum(self.nums[left: right+1])
        return self.log[left][right]


obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0, 2)
param_2 = obj.sumRange(2, 5)
param_3 = obj.sumRange(0, 5)

print(f"obj: {obj}, param1: {param_1}, param2: {param_2}, param3: {param_3}") #[null, 1, -1, -3]

