x = input()
y = input()
lis = [i for i in x]
lis.sort()
ans = ""
zero = ""
for i in lis:
    if i == "0":
        zero += i
    else:
        ans += i
if len(ans) > 0:
	ans = ans[0] + zero + ans[1:]
	ans = int(ans)
else:
    ans = "0"
if len(lis) != len(y):
    print("WRONG_ANSWER")
elif int(ans) == int(y):
    print("OK")
else:
    print("WRONG_ANSWER")