for _ in range(int(input())):
    x = int(input())
    s = input()
    left = 0
    right = x - 1
    change = 0
    while left < right:
        if change == 0:
            if s[left] != s[right]:
                change += 1
        elif change == 1:
            if s[left] == s[right]:
                change += 1
        elif change == 2:
            if s[left] != s[right]:
                change += 1
                print("No")
                break
        left += 1
        right -= 1
    if change < 3:
        print("Yes")