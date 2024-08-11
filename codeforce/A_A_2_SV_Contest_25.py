a, b, c, d = map(int, input().split())
def cal(point, time):
  return max((3 * point)/10, point - (point/250) * time)

Paulos = cal(a, c)
Mighty = cal(b, d)

if Mighty == Paulos:
  print("Tie")
elif Mighty > Paulos:
  print("Vasya")
else:
  print("Misha")