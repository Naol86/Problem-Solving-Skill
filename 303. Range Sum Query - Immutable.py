class NumArray:

    def __init__(self, nums: List[int]):
        temp = [0]
        for i in range(len(nums)):
            num = temp[i] + nums[i] 
            temp.append(num)
        print(temp)
        self.nums = temp
        

    def sumRange(self, left: int, right: int) -> int:
        ans = self.nums[right+1] - self.nums[left]
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)