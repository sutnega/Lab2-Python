def level3(n):
    res = 0
    while n > 0:
        res = (res*10) + (n % 10)
        n //= 10
    return res
print(level3(int(input("Введите число: "))))