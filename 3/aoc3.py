
if __name__ == "__main__":
    map_text = []
    # with open('3/sample.txt', 'r') as inFile:
    with open('3/input.txt', 'r') as inFile:
        for line in inFile:
            line = line.strip()
            map_text.append(200000 * [char for char in line])

    height = len(map_text)
    width = len(map_text[0])
    # r, c
    # 1, 1 = 64
    # 1, 3 = 284
    # 1, 5 = 71
    # 1, 7 = 68
    # 2, 1 = 40
    rows = 2
    cols = 1
    r = rows
    c = cols
    trees = 0
    while r < len(map_text):
        if c < len(map_text[0]) and r < len(map_text):
            if map_text[r][c] == '#':
                trees += 1
                map_text[r][c] = 'X'
            else:
                map_text[r][c] = 'O'
        r += rows
        c += cols

    # print(map_text)
    print('Total trees:', trees)
