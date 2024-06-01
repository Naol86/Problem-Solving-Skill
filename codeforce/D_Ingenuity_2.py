# from collections import Counter


# for _ in range(int(input())):
#   x = int(input())
#   s = input()
#   count = Counter(s)
#   if count['N'] % 2 != count['S'] % 2:
#     print("NO")
#     continue
#   if count["E"] % 2 != count['W'] % 2:
#     print("NO")
#     continue
#   # N S E W
#   r = [0,0,0,0]
#   h = [0,0,0,0]
#   index = {'N':0, "S":1, "E":2, "W":3}
#   opp = {'N':"S", 'S':"N", "E":'W', 'W':'E'}
#   odd = 0
#   for key, value in count.items():
#     if value % 2 == 1:
#       if odd % 2:
#         r[index[key]] += 1
#         r[index[opp[key]]] += 1
#         value -= 1
#         count[opp[key]] -= 1
#       else:
#         h[index[key]] += 1
#         h[index[opp[key]]] += 1
#         value -= 1
#         count[opp[key]] -= 1
#       odd += 1
#     r[index[key]] += value//2
#     h[index[key]] += value//2
#   ans = []
#   r_count = 0
#   for key in s:
#     if r[index[key]]:
#       ans.append("R")
#       r[index[key]] -= 1
#       r_count += 1
#     else:
#       ans.append("H")
#       h[index[key]] -= 1
#   if r_count > 0 and r_count < len(ans):
#     print(''.join(ans))
#   else:
#     print("NO")

for i in range(1, 51):
  print(i, i//2)