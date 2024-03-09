for _ in range(int(input())):
    x = input()
    lis = [int(i) for i in x]
    if len(lis) == 1:
        print(x)
    else:
        odd = [lis[0] if lis[0] % 2 != 0 else -1]
        even = [lis[0] if lis[0] % 2 == 0 else -1]
        # odd.append(max(odd[-1], lis[1]) if lis[1] % 2 != 0 else -1)
        # even.append(max(even[-1], lis[1]) if lis[1] % 2 == 0 else -1)

        left = 0
        right = 1

        while right < len(lis):
            odd.append(max(odd[-1], lis[right]) if lis[right] % 2 != 0 else -1)
            even.append(max(even[-1], lis[right]) if lis[right] % 2 == 0 else -1)
            if lis[left] % 2 != lis[right] % 2:
                temp_left = left
                temp_right = right
                while temp_left >= 0 and lis[temp_left] % 2 != lis[temp_right] % 2:
                    if lis[temp_right] % 2 == 0:
                        if odd[temp_left] > lis[temp_right]:
                            lis[temp_left], lis[temp_right] = lis[temp_right], lis[temp_left]
                            temp_left -= 1
                            temp_right -= 1
                        else:
                            break
                    elif lis[temp_right] % 2 != 0:
                        if even[temp_left] > lis[temp_right]:
                            lis[temp_left], lis[temp_right] = lis[temp_right], lis[temp_left]
                            temp_left -= 1
                            temp_right -= 1
                        else:
                            break
            left += 1
            right += 1

        print(''.join([str(i) for i in lis]))