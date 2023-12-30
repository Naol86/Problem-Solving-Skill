for _ in range(int(input())):
    s = input()
    upper_case = []
    lower_case = []
    ans = []
    for i in range(len(s)):
        if s[i] == 'B':
            ans.append('')
            if len(upper_case) > 0 and len(ans) > 0:
                ans[upper_case[-1]] = ''
                upper_case.pop()
        elif s[i] == 'b':
            ans.append('')
            if len(lower_case) > 0 and len(ans) > 0:
                ans[lower_case[-1]] = ''
                lower_case.pop()
        elif s[i].isupper():
            ans.append(s[i])
            upper_case.append(i)
        elif s[i].islower():
            ans.append(s[i])
            lower_case.append(i)
    print("".join(ans))