N = int(input())
S = [input() for i in range(N)]

def reverse(s):
   return s[::-1]

isKaibun = False

for i in range(N):
    for j in range(N):
      if i == j:
        continue
      str = S[i] + S[j]
      reversed = reverse(str)
      if str == reversed:
         isKaibun = True

print('Yes' if isKaibun else 'No')
