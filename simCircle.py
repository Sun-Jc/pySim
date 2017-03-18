import random

UP = 2
DOWN = 1
N = 100000000


def go(up, down):
    cur = 0
    while cur != up + 1 and cur != -down - 1:
        if random.random() < 0.5:
            cur += 1
        else:
            cur -= 1
        yield cur

count = [0] * (UP + DOWN + 3)

for i in range(0, N):
    for x in go(UP, DOWN):
        # print(x)
        count[DOWN + 1 + x] += 1

l = list(map(lambda x: x/N, count))
print(l[DOWN], l[DOWN + 2])
