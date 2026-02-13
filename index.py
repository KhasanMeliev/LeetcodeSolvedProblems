def func(n):
    if int(n**(1/2)) == n**(1/2):
        return 1
    while not n % 4:
        n //= 4
    if n % 8 == 7:
        return 4

    i = 1
    while i*i < n:
        if (n-i*i)**(1/2) == int((n-i*i)**(1/2)):
            return 2
        i += 1

    return 3


print(func(1103272344472637627))
