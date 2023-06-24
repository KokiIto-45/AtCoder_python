from copy import deepcopy

N = int(input())
S = list(input())

isContinue = True


def trimBrackets(array):
    for i in range(len(array)):
      if array[i] =='(':
          startIdx = i
          endIdx = i
          for j in range(i+1, len(array)):
              if array[j] == '(':
                  break
              elif array[j] ==')':
                  endIdx = j+1
          if startIdx != endIdx:
              del array[startIdx:endIdx]
              return array
    return array


while True:
    tmp = deepcopy(S)
    S = trimBrackets(S)
    if tmp == S:
        break


ansStr = ''
for i in range(len(S)):
    ansStr += S[i]

print(ansStr)

        
