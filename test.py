# def compute_lps(pattern):
#     lps = [0] * len(pattern)
#     length = 0
#     i = 1
#     while i < len(pattern):
#         if pattern[i] == pattern[length]:
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length - 1]
#             else:
#                 lps[i] = 0
#                 i += 1
#     return lps
# print(compute_lps('ababcab'))

import random


lis = []
for _ in range(1000):
    x = random.randint(1, 200)
    lis.append(x)
print(lis)