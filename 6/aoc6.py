
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


def count_people(q):
    return len(q)


def count_answers(q):
    answers = set()
    for person in q:
        ans = [ch for ch in person]
        for r in ans:
            answers.add(r)

    return len(answers)


def count_common_answers(q):
    people = []
    for person in q:
        people.append(set([ch for ch in person]))
    intersection = set.intersection(*people)
    return len(intersection)


if __name__ == "__main__":
    groups = []
    # with open('6/sample.txt', 'r') as inFile:
    with open('6/input.txt', 'r') as inFile:
        groups = list(map(str.strip, inFile.readlines()))

    groups = remove_empty(split_list(groups))
    all_uniques = []
    for question in groups:
        #a = count_answers(question)
        a = count_common_answers(question)
        all_uniques.append(a)
        print(question)
        print("unique answers", a)

    print("total:", sum(all_uniques))
