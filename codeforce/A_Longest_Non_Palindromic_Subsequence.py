import sys

# input = sys.stdin.readline

for _ in range(int(input())):
    s = input()
    left = 0
    right = len(s) - 1
    pal = True
    while right > left:
        if s[left] != s[right]:
            pal = False
            break
        left += 1
        right -= 1
    if not pal:
        print(len(s))
    else:
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                print(len(s) - 1)
                break
        else:
            print(-1)