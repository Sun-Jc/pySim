import random
N = 100
M = 100
C = 5


# clique generator
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


# random walker
def walk(s, t, neighbors):
    cur = s
    yield cur
    while cur != t:
        next_neighbor = random.randint(0, len(neighbors[cur]) - 1)
        cur = neighbors[cur][next_neighbor]
        yield cur


# stat init
def init_random_walk():
    random_walk_count = {}
    for i in nodes:
        random_walk_count[i] = 0
    return random_walk_count


# random walk stat
def random_walk(neighbors):
    random_walk_count = init_random_walk()
    for s in nodes:
        for t in nodes:
            # print(s, t)
            random_walk_this = init_random_walk()
            for x in range(0, M):
                for i in walk(s, t, neighbors):
                    if True:#i != s and i != t:
                        random_walk_this[i] += 1
            random_walk_count = dict(map(lambda k: (k, random_walk_count[k] + random_walk_this[k] / M)
                                         , random_walk_count))
    return random_walk_count


if __name__ == "__main__":
    # Create graph
    neighbors = {'a': [], 'b': []}
    for pair in create_clique('b', C):
        a = pair[0]
        b = pair[1]
        if pair[1] is int:
            b = chr(pair[1])
        neighbors[a] = neighbors.get(a, []) + [b]
    for pair in create_clique('a', C):
        a = pair[0]
        b = pair[1]
        if pair[1] is int:
            b = chr(pair[1])
        neighbors[a] = neighbors.get(a, []) + [b]

    neighbors['w'] = []
    neighbors['v'] = []
    neighbors['u'] = []
    neighbors['v'] += ['a', 'w']
    neighbors['w'] += ['v', 'b']

    neighbors['u'] += ['a', 'b']
    neighbors['a'] += ['v', 'u']
    neighbors['b'] += ['w', 'u']

    print(neighbors)

    nodes = neighbors.keys()

    # compute random walk
    random_walk_sum = init_random_walk()
    for i in range(0, N):
        r = random_walk(neighbors)
        for j in r.keys():
            random_walk_sum[j] += r[j]

    random_walk_sum = dict(map(lambda k: (k, random_walk_sum[k]/N), random_walk_sum))

    print('u', random_walk_sum['u'])
    print('v', random_walk_sum['v'])
    print('w', random_walk_sum['w'])
