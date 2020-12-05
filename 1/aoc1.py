import itertools


def check_constraint(x, y, z):
    if (x + y + z) == 2020:
        print(x * y * z)


if __name__ == "__main__":
    expenses = []
    N = 3
    # with open('sample.txt', 'r') as inFile:
    with open('input1.txt', 'r') as inFile:
        for line in inFile:
            expenses.append(int(line.strip()))

    for pair in itertools.combinations(expenses, r=N):
        check_constraint(*pair)
