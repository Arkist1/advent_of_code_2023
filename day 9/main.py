input = open("input.txt", "r").read()
print(input)


def parse_line(s):
    return [int(x.strip()) for x in s.split(" ")]


def parse_file(s):
    return [parse_line(x) for x in s.split("\n")]


def get_delta(s):
    res = []
    for index, x in enumerate(s[:-1]):
        res.append(s[index + 1] - s[index])

    return res


def all_0(lst):
    for x in lst:
        if x != 0:
            return False

    return True


def neg_sum(lst):
    res = 0
    for x in reversed(lst):
        print(res, x)
        res = x - res

    return res


def part_1(i):
    res = []
    for s in i:
        deltas = [s]

        while not all_0(deltas[-1]):
            deltas.append(get_delta(deltas[-1]))

        res.append(sum([d[-1] for d in deltas]))

    return res


def part_2(i):
    res = []
    for s in i:
        deltas = [s]

        while not all_0(deltas[-1]):
            deltas.append(get_delta(deltas[-1]))

        res.append(neg_sum([d[0] for d in deltas]))

    return res


parsed_input = parse_file(input)
print(parsed_input)

part_1_res = part_1(parsed_input)
# print(part_1_res)
print(sum(part_1_res))


part_2_res = part_2(parsed_input)
print(part_2_res)
print(sum(part_2_res))
