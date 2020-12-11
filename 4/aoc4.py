
def split_list(g):
    size = len(g)
    idx_list = [idx + 1 for idx, val in
                enumerate(g) if val == '']

    res = [g[i: j] for i, j in
           zip([0] + idx_list, idx_list +
               ([size] if idx_list[-1] != size else []))]

    return res


def remove_empty(g):
    new_g = []
    for l in g:
        new_g.append(list(filter(lambda x: x != '', l)))
    return new_g


def merge_lists(lst):
    new_lst = []
    for l in lst:
        new_lst.append(' '.join(l))
    return new_lst


if __name__ == "__main__":
    passports = []
    # with open('4/sample.txt', 'r') as inFile:
    with open('4/input.txt', 'r') as inFile:
        passports = list(map(str.strip, inFile.readlines()))

    passports = merge_lists(remove_empty(split_list(passports)))
    print(len(passports))
    print(passports)

    required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    other_fields = ['cid']

    valid = 0
    for p in passports:
        if all(rf in p for rf in required_fields):
            valid += 1
    print("Valid:", valid)
