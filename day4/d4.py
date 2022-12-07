nums = [[[int(x) for x in pair.split('-')] for pair in line.split(',')] for line in open('input.txt').read().split('\n')]

contained = 0
for n in nums:
    a, b = n
    if (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1]):
        contained += 1

print(contained)

overlap = 0
for n in nums:
    a, b = n
    a = set(range(a[0],a[1]+1))
    b = set(range(b[0],b[1]+1))
    if a.intersection(b):
        overlap += 1

print(overlap)