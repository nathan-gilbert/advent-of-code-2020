import re

pat = re.compile(r'(\d)-(\d)\s(\w):\s(\w+)')


def parse_requirements(ps):
    m = pat.match(ps)
    low = int(m.group(1))
    high = int(m.group(2))
    ch = m.group(3)
    password = m.group(4)

    return (low, high, ch, password)


if __name__ == "__main__":
    passwords = []
    with open('2/sample.txt', 'r') as inFile:
        for line in inFile:
            passwords.append(line.strip())

    for p in passwords:
        res = parse_requirements(p)
        print(res)
