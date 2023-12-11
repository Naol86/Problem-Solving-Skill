class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jump = nums[0]
        count = 1
        _max = 0
        _index = 0
        i = 0
        while jump > 0:
            i+=1
            jump -=1
            if i == len(nums)-1:
                return count
            # print(nums[i] - jump,"max is ",_max)
            if (nums[i] - jump) > _max:
                _max = nums[i] - jump
                _index = i
            if jump == 0:
                # print(_max,_index)
                jump = nums[_index]
                i = _index
                _max = 0
                count +=1
        return 0