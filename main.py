def digit(n):
    counter = 0
    for i in range(1, n+1):
        lst = [int(d) for d in str(i)]
        if 0 in lst:
            counter += 1
        else:
            continue
    return (counter)
n = int(input())
print(digit(n))
