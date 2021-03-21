T  = int(input())
for _ in range(T):
         from statistics import mode
         a = list(map(int, input().split()))
         print(mode(a))