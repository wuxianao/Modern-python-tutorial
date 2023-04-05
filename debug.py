def power(x, n): # 乘方
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#测试
print(power(3, 2))
print(power(2, 3))