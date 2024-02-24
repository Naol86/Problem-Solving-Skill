x = int(input())
lis = [int(i) for i in input().split()]
lis.sort()
ans = 0
left = 0
right = 1
while right < x and right > left:
    if lis[left] == 0:
        left += 1
    elif lis[left] < lis[right]:
        # lis[right] = 0
        ans += 1
        left += 1
        right += 1
    else:
        right += 1
    if left == right:
        right += 1
print(ans)


# ans = -1
# temp = -1
# for i in range(x - 1, -1,-1):
#     # print(lis)
#     if lis[i] > temp:
#         ans += 1
#         temp = lis[-1]
#         lis.pop()
#     elif lis[i] == temp and i != 0:
#         for j in range(i, -1, -1):
#             if lis[j] > temp:
#                 ans += 1
#                 temp = lis[j]
#                 lis.pop(j)
#                 break
#     else:
#         temp = lis[i]
# print(ans)