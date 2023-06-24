import numpy as np

INPUTS = [input() for i in range(2)]
N = int(INPUTS[0])
A = list(map(int, INPUTS[1].split()))

array = np.array_split(A, N)

ans = list(map(sum, array))

ansArray = ''

for i in range(len(ans)):
    ansArray += ' '
    ansArray += str(ans[i])

print(ansArray.strip())

