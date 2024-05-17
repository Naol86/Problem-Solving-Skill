import sys, threading


def main():
    # write your solution here
    for _ in range(int(input())):
      cache = {}
      x = int(input())
      nums = [int(i) for i in input().split()]
      def dp(i, temp):
        if i >= len(nums):
          return 0
        if i in cache:
          return cache[i]
        t = 0 if temp + i >= len(nums) else nums[i + temp]
        cache[i] = temp + dp(i + temp, t)
        return cache[i]
      _max = 0
      for i in range(x):
        _max = max(_max, dp(i, nums[i]))
        # print(_max, 'asd')
      print(_max)
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
