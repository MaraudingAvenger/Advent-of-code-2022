import re
from queue import Queue

stacks, moves = open('input.txt', 'r').read().split("\n\n")

stacks = stacks.split("\n")
n_stacks = len(stacks[-1].strip().split())
queues = {i: list() for i in range(1, n_stacks+1)}

for stack in stacks:
    print(stack)
print()

# build queues
for line in stacks[:-1]:
    q = 1
    i = 0
    while q <= n_stacks:
        box = line[i:i+4].strip().strip("[").strip(']')
        if box:
            # print(f"{q} -> {box}")
            queues[q].insert(0,box)
        q += 1
        i += 4

pattern = re.compile(r"move (\d{1,3}) from (\d{1,2}) to (\d{1,2})")
moves = moves.split("\n")
for move in moves:
    n, origin, destination = pattern.match(move).groups()
    n = int(n)
    origin = int(origin)
    destination = int(destination)
    for _ in range(n):
        queues[destination].append(queues[origin].pop())

print("part 1:", end=' ')
for queue in queues.values():
    print(f"{queue[-1]}", end='')
print()

# rebuild queues
queues = {i: list() for i in range(1, n_stacks+1)}
for line in stacks[:-1]:
    q = 1
    i = 0
    while q <= n_stacks:
        box = line[i:i+4].strip().strip("[").strip(']')
        if box:
            queues[q].insert(0,box)
        q += 1
        i += 4

for move in moves:
    n, origin, destination = pattern.match(move).groups()
    n = int(n)
    origin = int(origin)
    destination = int(destination)
    to_stay, to_move = queues[origin][:-n], queues[origin][-n:]
    queues[origin] = to_stay
    queues[destination].extend(to_move)

print('part 2:', end=' ')
for queue in queues.values():
    print(f"{queue[-1]}", end='')