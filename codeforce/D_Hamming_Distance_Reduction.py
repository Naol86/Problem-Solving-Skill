from collections import defaultdict
import sys
input = sys.stdin.readline

x = int(input())
S = input()
T = input()

s_swap = defaultdict(list)
t_swap = defaultdict(list)
hamming_dis = 0

for i in range(x):
    if S[i] != T[i]:
        if len(s_swap[S[i]]) < 3:
            s_swap[S[i]].append(i)
        t_swap[T[i]].append(i)
        hamming_dis += 1

_max = 0
index = [-1, -1]
def call():
    _max = 0
    index = [-1, -1]
    for key in s_swap:
        if key not in t_swap:
            continue
        else:
            for val in s_swap[key]:
                for value in t_swap[key]:
                    if T[val] == S[value]:
                        index = [value + 1, val + 1]
                        _max = 2
                        return (_max, index)
                    else:
                        _max = 1
                        index = [value + 1, val + 1]
    return (_max, index)

_max, index = call()

print(hamming_dis - _max)
print(*index)