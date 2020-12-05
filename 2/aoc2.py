import re

pat = re.compile(r'(\d+)-(\d+)\s(\w):\s(\w+)')


def parse_requirements(ps):
    m = pat.match(ps)
    low = int(m.group(1))
    high = int(m.group(2))
    ch = m.group(3)
    password = m.group(4)

    return (low, high, ch, password)


def valid(low, high, ch, password):
    count = password.count(ch)
    if low <= count <= high:
        return True
    else:
        return False


if __name__ == "__main__":
    passwords = []
    with open('2/sample.txt', 'r') as inFile:
        # with open('2/input.txt', 'r') as inFile:
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
        filter(None, [valid(*parse_requirements(p)) for p in passwords]))
    print(len(results))
