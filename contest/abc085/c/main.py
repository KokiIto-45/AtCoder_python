inputs = list(map(int,input().split()))

N = inputs[0]
Y = inputs[1]

ans10000 = -1
ans5000 = -1
ans1000 = -1

for a in range(N+1):
    for b in range(N-a+1):
        c = N - a - b 
        total = 10000*a + 5000*b + 1000*c
        if total == Y:
            ans10000 = a
            ans5000 = b
            ans1000 = c

print(str(ans10000) + " " + str(ans5000) + " " + str(ans1000))