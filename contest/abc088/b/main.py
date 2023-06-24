input = [input() for i in range(2)]
N = input[0]
Cards = list(map(int, input[1].split()))

Alice = 0
Bob = 0

if len(Cards) % 2 == 1:
    idx = Cards.index(min(Cards))
    lastNum = Cards.pop(idx)
    Alice += lastNum

turns = len(Cards) / 2
for i in range(int(turns)):
    first = Cards.index(max(Cards))
    largerNum = Cards.pop(first)
    Alice += largerNum

    second = Cards.index(max(Cards))
    smallerNum = Cards.pop(second)
    Bob += smallerNum

print(Alice - Bob)
    