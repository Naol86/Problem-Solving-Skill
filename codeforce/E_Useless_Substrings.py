x = input()
t = input()

upper = 0
lower = 0

ans = 0
while upper < len(x):
    if x[upper] == t[lower]:
        lower += 1
    else:
        if lower > 0:
            upper -= 1
        lower = 0
    upper += 1
    if lower == len(t):
        right = len(x) - upper
        left = upper - len(t)
        ans = max(right, left)
        lower = 0
        # break
print(ans)