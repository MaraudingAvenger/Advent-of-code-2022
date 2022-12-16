lines = [[int(i) for i in line] for line in open('input.txt').read().split()]

def look_up(x, y, lines=lines):
    if x == 0 or y == 0 or x == len(lines)-1 or y == len(lines[0])-1:
        return True
    return all(item < lines[x][y] for item in map(lambda k: k[y], lines[:x]))

def look_down(x, y, lines=lines):
    if x == 0 or y == 0 or x == len(lines)-1 or y == len(lines[0])-1:
        return True
    return all(item < lines[x][y] for item in map(lambda k: k[y], lines[x+1:]))

def look_left(x, y, lines=lines):
    if x == 0 or y == 0 or x == len(lines)-1 or y == len(lines[0])-1:
        return True
    return all(item < lines[x][y] for item in lines[x][:y])

def look_right(x, y, lines=lines):
    if x == 0 or y == 0 or x == len(lines)-1 or y == len(lines[0])-1:
        return True
    return all(item < lines[x][y] for item in lines[x][y+1:])

def is_visible(x, y, lines=lines):
    return look_up(x, y) or look_down(x, y) or look_left(x, y) or look_right(x, y)


def count_up(x, y, lines=lines):
    if y == 0:
        return 0
    count = 0
    for i in range(y-1, -1, -1):
        if lines[i][x] >= lines[y][x]:
            count += 1
            return count
        count += 1
    return count

def count_down(x, y, lines=lines):
    if y == len(lines[0])-1:
        return 0
    count = 0
    for i in range(y+1, len(lines)):
        if lines[i][x] >= lines[y][x]:
            count += 1
            return count
        count += 1
    return count

def count_left(x, y, lines=lines):
    if x == 0:
        return 0
    count = 0
    for i in range(x-1, -1, -1):
        if lines[y][i] >= lines[y][x]:
            count += 1
            return count
        count += 1
    return count

def count_right(x, y, lines=lines):
    if x == len(lines)-1:
        return 0
    count = 0
    for i in range(x+1, len(lines)):
        if lines[y][i] >= lines[y][x]:
            count += 1
            return count
        count += 1
    return count

def scenic_score(x, y, lines=lines):
    return count_up(x, y) * count_down(x, y) * count_left(x, y) * count_right(x, y)

if __name__ == "__main__":
    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            total += is_visible(x, y)
    print(f"Part 1: visible trees = {total}")

    print(f"Part 2: most scenic tree score = {max(map(max, [[scenic_score(x, y) for x in range(len(lines))] for y in range(len(lines[0]))]))}")