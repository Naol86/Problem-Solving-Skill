for _ in range(int(input())):
    word = input()
    leng = len(word)
    if leng > 10:
        print(f"{word[0]}{leng-2}{word[-1]}")
    else:
        print(word)