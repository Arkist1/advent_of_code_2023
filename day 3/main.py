import string

input = open("input.txt", "r").read()

print(input)


def parse_line(line):
    return [int(x) if x in string.digits else x for x in line]


def parse_matrix(matrix):
    return [parse_line(x) for x in matrix.split("\n")]


def look_around(m, index):
    res = []
    start_y = max(0, index[0] - 1)
    stop_y = min(len(m), index[0] + 2)
    range_y = range(start_y, stop_y)

    start_x = max(0, index[1] - 1)
    stop_x = min(len(m[index[0]]), index[1] + 2)
    range_x = range(start_x, stop_x)

    for y in range_y:
        for x in range_x:
            if [y, x] == index:
                continue

            res.append(m[y][x])

    return res


def hashed_look_around(m, index):
    res = {}
    start_y = max(0, index[0] - 1)
    stop_y = min(len(m), index[0] + 2)
    range_y = range(start_y, stop_y)

    start_x = max(0, index[1] - 1)
    stop_x = min(len(m[index[0]]), index[1] + 2)
    range_x = range(start_x, stop_x)

    for y in range_y:
        for x in range_x:
            if [y, x] == index:
                continue

            res[y, x] = m[y][x]

    return res


def part_1(m):
    pos = []
    for y, row in enumerate(m):
        curr = []
        for x, sample in enumerate(row + ["."]):
            if isinstance(sample, int):
                curr.append([y, x])
            else:
                res = []
                number = 0

                for index, coords in enumerate(curr):
                    number += m[coords[0]][coords[1]] * 10 ** (len(curr) - index - 1)
                    for t in look_around(m, coords):
                        res.append(t)

                for token in res:
                    if isinstance(token, str):
                        if not token == ".":
                            pos.append(number)
                            break

                curr = []

    return pos


def part_2(m):
    pos = {}
    for y, row in enumerate(m):
        curr = []
        for x, sample in enumerate(row + ["."]):
            if isinstance(sample, int):
                curr.append([y, x])
            else:
                res = {}
                number = 0

                for index, coords in enumerate(curr):
                    number += m[coords[0]][coords[1]] * 10 ** (len(curr) - index - 1)
                    for index, value in hashed_look_around(m, coords).items():
                        res[index] = value

                for index, token in res.items():
                    if isinstance(token, str):
                        if token == "*":
                            if index in pos:
                                pos[index].append(number)
                            else:
                                pos[index] = [number]

                curr = []

    res = []
    for index, value in pos.items():
        if len(value) == 2:
            res.append(value[0] * value[1])

    return res


parsed_input = parse_matrix(input)

print(parsed_input)

part_1_res = part_1(parsed_input)
print(part_1_res)
print(sum(part_1_res))


part_2_res = part_2(parsed_input)
print(part_2_res)
print(sum(part_2_res))
