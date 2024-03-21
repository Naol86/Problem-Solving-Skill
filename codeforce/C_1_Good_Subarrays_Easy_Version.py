for _ in range(int(input())):
    x = int(input())
    nums = [int(i) for i in input().split()]

    def find(nums):
        prev = 0
        left = 0
        right = 0
        ans = 0
        while right < len(nums):
            # print(left, right)
            if nums[right] < right - left + 1:
                ans += (right - left) * (right - left + 1) // 2 - (prev * (prev + 1) // 2)
                prev = right - left - 1
                # print(ans, ' this is prev')
                left += 1
            else:
                right += 1
                prev -= 1 if prev > 0 else 0
            # print(ans)
        ans += (right - left) * (right - left + 1) // 2 - (prev * (prev + 1) // 2)
        return ans
    ans = find(nums)
    print(ans)