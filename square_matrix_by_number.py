
# If input is a square number of required dimension of number then code prints square matrix
n = int(input())
for j in range(int(n**(1/2))):
    for i in range(int(n ** (1 / 2))):
        print((i + 1) + j * int(n ** (1 / 2)), end=" ")
    print()

# If input is a number of required dimension of number then code prints square matrix upto square of number
m = int(input())
for j in range(m):
    for i in range(m):
        print((i + 1) + j * int(m), end=" ")
    print()
