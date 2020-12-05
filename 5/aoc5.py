from math import floor, ceil


def parse_row(row_str, p):
    if row_str == '':
        return p

    if row_str[0] == 'F' or row_str[0] == 'L':
        new_p1 = floor((p[1] + p[0]) / 2)
        p = (p[0], new_p1)
    else:
        new_p0 = p[0] + ceil((p[1] - p[0]) / 2)
        p = (new_p0, p[1])

    p = parse_row(row_str[1:], p)
    return p


def parse_column(col_str):
    return parse_row(col_str, (0, 7))


def get_seat_id(r, c):
    return (r * 8) + c


def find_my_seat_id(lst):
    lst = sorted(lst)
    return [x for x in range(lst[0], lst[-1]+1)
            if x not in lst]


if __name__ == "__main__":
    bpasses = []
    # with open('5/sample.txt', 'r') as inFile:
    with open('5/input.txt', 'r') as inFile:
        bpasses = list(map(str.strip, inFile.readlines()))

    seat_ids = []
    for bp in bpasses:
        row = parse_row(bp[:7], (0, 127))
        # if row[0] == row[1]:
        #    print(row[0])
        # else:
        #    raise Exception('row is incorrect')

        col = parse_column(bp[-3:])
        # if col[0] == col[1]:
        #    print(col[0])
        # else:
        #    raise Exception('col is incorrect')

        seat_id = get_seat_id(row[0], col[0])
        # print(seat_id)
        seat_ids.append(seat_id)

    max_seat_id = max(seat_ids)
    print("max seat id: ", max_seat_id)

    b = find_my_seat_id(seat_ids)
    print(b)
