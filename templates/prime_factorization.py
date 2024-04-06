def prime_fac(n: int):
    res = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            res.append(i)
            n //= i
        i += 1
    if n > 1:
        res.append(n)
    return res