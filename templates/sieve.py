def prime_sieve(n):
    res = [True] * (n + 1)

    res[0] = res[1] = False

    i = 2
    while i * i <= n:
        if res[i]:
            j = i * i
            while j <= n:
                res[j] = False
                j += i
        i += 1

    return res