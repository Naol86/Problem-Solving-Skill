for _ in range(int(input())):
    lis = input()
    hour = int(lis[:2])
    if hour < 12:
        if hour == 0:
            print(f"{12}:{lis[3:]} AM")
        else:
            print(lis, "AM")
    else:
        if hour == 12:
            print(lis, "PM")
        else:
            temp = 0 if hour < 22 else ''
            print(f"{temp}{hour - 12}:{lis[3:]} PM")