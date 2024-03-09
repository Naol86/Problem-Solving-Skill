import sys 

input = sys.stdin.readline

lis = input()

_max = 0
freq = 1

stack = [-1]

for i in range(len(lis)):
    if lis[i] == ')':
        stack.pop()
        if stack:
            leng = i - stack[-1]
            if leng > _max:
                _max = leng
                freq = 1
            elif leng == _max:
                freq += 1
        else:
            stack.append(i)
    else:
        stack.append(i)
print(_max, freq)