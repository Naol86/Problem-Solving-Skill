import heapq
import sys, threading


def main():
    # write your solution here
    n, a, b, c = map(int, input().split())
    lis = [a, b, c]
    ans = [0]
    cache = {}
    def cutting(left, cut):
      if left == 0:
        return 0
      if left < 0:
        return -float('inf')
      if left in cache:
        return cache[left]
      y = -float('inf')
      for i in lis:
        temp = cutting(left - i, cut + 1)
        y = max(y, temp)
      cache[left] = y + 1
      return cache[left]
    print(cutting(n, 0))
    # print(cache)
    # print(*ans)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
