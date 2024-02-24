x, y = [int(i) for i in input().split()]

while x <= y:
    temp = set([i for i in str(x)])
    if len(temp) == len(str(x)):
        print(x)
        break
    else:
        x += 1
if x > y:
    print(-1)



# lis_x = [int(i) for i in x]
# _set = set()
# ans = []
# i = 0
# while i < len(lis_x) and len(ans) <= len(y):
#     if lis_x[i] not in _set:
#         ans.append(str(lis_x[i]))
#         _set.add(lis_x[i])
#         i += 1
#     else:
#         if lis_x[i] == 9:
#             if i != 0:
#                 lis_x[i] = 0
#                 _set.remove(lis_x[i-1])
#                 lis_x[i-1] += 1
#                 i -= 1
#             else:
#                 lis_x[i] = 0
#                 lis_x.append(0)
#                 for i in range(len(lis_x)):
#                     if i == 0:
#                         lis_x[i] = 1
#                     else:
#                         lis_x[i] = 0
#                 i = 0
#                 _set = set()
#         else:
#             lis_x[i] += 1
# if int(''.join(ans)) <= int(y):
#     print(''.join(ans))
# else:
#     print(-1)
# print(ans)