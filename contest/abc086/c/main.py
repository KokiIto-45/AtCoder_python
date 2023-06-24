# ---解答例---

# # 奇数偶数
# N = int(input())
# X = 0
# Y = 0
# T = 0
# for i in range(N):
#   t, x, y = map(int, input().split())
#   dis = abs(X-x)+abs(Y-y)
#   if dis > t-T or not (T-t-dis)%2 == 0:
#     print('No')
#     exit()
#   T = t
#   X = x
#   Y = y
# print('Yes')