import string

with open('input.txt') as f:
    lines = f.read().split()

def score(letter:str) -> int:
    if letter in string.ascii_lowercase:
        return ord(letter) - 96
    elif letter in string.ascii_uppercase:
        return ord(letter) - 38
    return 0

total = 0
for line in lines:
    left, right = line[:len(line)//2], line[len(line)//2:]
    total += sum(map(score, {l for l in left if l in right}))

print(total)


badge_total = 0
for i in range(0, len(lines), 3):
    group = lines[i:i+3]
    for letter in set(group[0]):
        if all(letter in line for line in group[1:]):
            badge_total += score(letter)

print(badge_total)