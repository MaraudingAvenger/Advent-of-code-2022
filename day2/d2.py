input_converter = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3, # scissors
    'X': 1, # rock / lose
    'Y': 2, # paper / tie
    'Z': 3  # scissors / win
}

def convert_line(line:str) -> tuple:
    '''
    return opponent score, my score, match score
    '''
    a, b = map(input_converter.get, line.split(' '))
    return a, b

def score_line(line:str, converter=convert_line) -> int:
    opponent, me = converter(line)
    if opponent == me:
        return me + 3
    beats={1:3, 2:1, 3:2}
    if beats[opponent] == me:
        return me
    return me + 6

def convert_line2(line:str) -> tuple[int,int]:
    '''
    return opponent score, my score, match score
    '''
    a, b = convert_line(line)
    if b == 2:
        return a, a
    loses = {1:3, 2:1, 3:2}
    beats = {1:2, 2:3, 3:1}
    return a, {1: loses, 3: beats}[b][a]

if __name__ == '__main__':
    lines = [l.strip() for l in open('input.txt').readlines() if l.strip()]

    print(sum(score_line(line) for line in lines))
    print(sum(score_line(line, converter=convert_line2) for line in lines))