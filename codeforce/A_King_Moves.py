position = input()
count = 8
if position[0] == 'a' or position[0] == 'h' :
    count -= 3
if position[1] == '1' or position[1] == '8':
    count -= 3
if (position[1] == '1' or position[1] == '8') and (position[0] == 'a' or position[0] == 'h'):
    count += 1
print(count)