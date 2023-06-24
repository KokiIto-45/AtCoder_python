S = list(input())

print(S)

T = ""

isEqual = False

# while not isEqual:
T1 = list(T + "dream")
T2 = list(T + "dreamer")
T3 = list(T + "erase")
T4 = list(T + "eraser")
candidates = [T1, T2, T3, T4]
for candidate in candidates:
    print(candidate)
    for i in len(candidate):
        if S[i] != candidate[i]:
            break

# ---解答例---
# S = input()
# while True:
#     if S.endswith("dream"):
#         S = S[:-5]
#     elif S.endswith("dreamer"):
#         S = S[:-7]
#     elif S.endswith("erase"):
#         S = S[:-5]
#     elif S.endswith("eraser"):
#         S = S[:-6]
#     elif S == "":
#         print("YES")
#         break
#     elif S != "":
#         print("NO")
#         break