def sumTen(a):
    if a==1:
        return 1
    else:
        return a+(sumTen(a-1))
print(sumTen(10))