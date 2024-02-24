x = int(input())
cap = int(input())
lis = []
for _ in range(x):
    lit = int(input())
    lis.append(lit)

lis.sort(reverse=True)
ans = 0
_sum = 0
i = 0
while cap > _sum:
    cap -= lis[i]
    i += 1
    ans += 1

print(ans)