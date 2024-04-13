import bisect
import sys

input = sys.stdin.readline

for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  left = 0
  right = x - 1
  bob = 0
  alice = 0
  
