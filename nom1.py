def level1(n):
    temp = n
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if(temp == rev):
        print("Это палиндром")
    else:
        print("Это не палиндром")
level1(5115)