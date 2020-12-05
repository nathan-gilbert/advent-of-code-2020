import re

pat = re.compile(r'(\d+)-(\d+)\s(\w):\s(\w+)')


def parse_requirements(ps):
    m = pat.match(ps)
    low = int(m.group(1))
    high = int(m.group(2))
    ch = m.group(3)
    password = m.group(4)

    return (low, high, ch, password)


def valid1(low, high, ch, password):
    count = password.count(ch)
    if low <= count <= high:
        return True
    else:
        return False


def letter_check(password, ch, position):
    return password[position-1] == ch


def valid2(first, second, ch, password):
    r = [letter_check(password, ch, first),
         letter_check(password, ch, second)]
    return len(list(filter(None, r))) == 1


if __name__ == "__main__":
    passwords = []
    # with open('2/sample.txt', 'r') as inFile:
    with open('2/input.txt', 'r') as inFile:
        for line in inFile:
            passwords.append(line.strip())

    # for p in passwords:
    #     res = parse_requirements(p)
    #     print(res)
    #     if valid(*res):
    #         print("Valid!")
    #     else:
    #         print("Not Valid!")

    results = list(
        filter(None, [valid2(*parse_requirements(p)) for p in passwords]))
    print(len(results))
