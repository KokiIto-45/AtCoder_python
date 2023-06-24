N = int(input())
mochis = [int(input()) for i in range(N)]

identicalMochis = list(set(mochis))

print(len(identicalMochis))