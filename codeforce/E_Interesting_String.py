from collections import Counter, defaultdict
strings = []
for _ in range(int(input())):
    s = input()
    strings.append([i for i in s])

for s in strings:
    order = []
    _set = set()
    for i in range(len(s) - 1, -1, -1):
        if s[i] not in _set:
            order.append(s[i])
            _set.add(s[i])
    order = order[::-1]
    counter = Counter(s)
    comp = {order[i]:counter[order[i]]//(i+1) for i in range(len(order))}
    # print(counter, comp)
    win = defaultdict(int)
    i = 0
    k = 0
    # print(order)
    che = True
    next = []
    res = -1
    for j in range(len(order)):
        # print(comp,"sdfasdfasdf")
        while win != comp and i < len(s):
            win[s[i]] += 1
            if s[i] != order[j]:
                next.append(s[i])
            i += 1
        # print(s[k:i])
        if win == comp and j == 0:
            ans = "".join(s[:i])
            res = "".join(s[:i])
            # print(win, "".join(s[:i]))
        elif win == comp and next
        else:
            print(-1)
            che = False
            break
        # print(j)
        k = i
        comp.pop(order[j])
        win = defaultdict(int)
    if che:
        print(''.join(s))
    # print(ans)