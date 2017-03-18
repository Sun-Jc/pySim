import random
N = 10
M = 1000
C = 5
L = 2


def create_clique(a_or_b, size):
    size -= 1
    for i in range(0, size):
        if a_or_b == 'a':
            yield ('a', i+1)
        else:
            yield ('b', -(i+1))
    for i in range(0, size):
        if a_or_b == 'a':
            yield (i+1, 'a')
        else:
            yield (-(i+1), 'b')
        for j in range(0, size):
            if i != j:
                if a_or_b == 'a':
                    yield (i+1, j+1)
                else:
                    yield (-(i+1), -(j+1))


def create_bridge(s,t, length):
    yield ('x0', [s, 'x1'])
    yield ("x"+str(length-1), [t, "x"+str(length-2)])
    for i in range(1,length-1):
        yield ("x"+str(i), ["x"+str(i-1), "x"+str(i+1)])

neighbors = {'a': [],
             'b': []}

for pair in create_clique('a', C):
    a = pair[0]
    b = pair[1]
    if pair[1] is int:
        b = chr(pair[1])
    neighbors[a] = neighbors.get(a, []) + [b]

for pair in create_clique('b', C):
    a = pair[0]
    b = pair[1]
    if pair[1] is int:
        b = chr(pair[1])
    neighbors[a] = neighbors.get(a, []) + [b]

neighbors['w'] = []
neighbors['v'] = []
neighbors['u'] = []
neighbors['v'] += ['a', 'x0']
neighbors['w'] += ['x'+str(L-1), 'b']
neighbors['u'] += ['a', 'b']
neighbors['a'] += ['v', 'u']
neighbors['b'] += ['w', 'u']

for x in create_bridge('v','w', L):
    neighbors[x[0]] = x[1]

print(neighbors)

nodes = neighbors.keys()


def walk(s, t):
    cur = s
    yield cur
    while cur != t:
        # random.seed()
        next_neighbor = random.randint(0, len(neighbors[cur])-1)
        cur = neighbors[cur][next_neighbor]
        yield cur


def init_random_walk():
    random_walk_count = {}
    for i in nodes:
        random_walk_count[i] = 0
    return random_walk_count


def random_walk():
    random_walk_count = init_random_walk()
    for s in nodes:
        for t in nodes:
            # print(s, t)
            random_walk_this = init_random_walk()
            for x in range(0, M):
                for i in walk(s, t):
                    if i != s and i != t:
                        random_walk_this[i] += 1
            for x in random_walk_this.keys():
                random_walk_count[x] += random_walk_this[x] / M
    return random_walk_count


random_walk_sum = init_random_walk()
for i in range(0, N):
    r = random_walk()
    for j in r.keys():
        random_walk_sum[j] += r[j]

for i in random_walk_sum.keys():
    random_walk_sum[i] /= N

print('u', random_walk_sum['u'])
print('v', random_walk_sum['v'])
print('w', random_walk_sum['w'])
