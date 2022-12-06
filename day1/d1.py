with open('input.txt') as f:
    elves = []
    while True:
        elf = []
        while not (line := f.readline().strip()) == "":
            elf.append(int(line))
        if not elf:
            break
        elves.append(elf)

# Part 1

ind, total = max([(i, sum(elf)) for i, elf in enumerate(elves,start=1)], key=lambda x: x[1])
print(f"Day1, Part 1 -- {ind}-th elf has the most calories: {total:,}")

# Part 2

top3 = sorted([(i, sum(elf)) for i, elf in enumerate(elves,start=1)], key=lambda x: x[1], reverse=True)[:3]
print(f"Day1, Part 2 -- Top 3 elves: {sum(map(lambda x: x[1], top3)):,}")