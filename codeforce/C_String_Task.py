lis = [i for i in input()]

for i in range(len(lis)):
    if lis[i] in {"A", "O", "Y", "E", "U", "I", 'a', 'o', 'y', 'e', 'u', 'i'}:
        lis[i] = ''
    else:
        lis[i] = lis[i].lower()
        lis[i] = '.' + lis[i]
print(''.join(lis))