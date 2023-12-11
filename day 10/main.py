input = open("input.txt", "r").read()
print(input)


joints = {
    "|": [[-1, 0], [1, 0]],
    "-": [[0, -1], [0, 1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    ".": [],
    "S": [],
}


def get_realtive(s1, s2):
    return [s1[0] - s2[0], s1[1] - s2[1]]


def find_start(s):
    for y in range(len(s)):
        for x in range(len(s[0])):
            if s[y][x] == "S":
                return [y, x]


def get_surrounding(s, p):
    res = []
    for y in range(max(0, p[0] - 1), min(len(s), p[0] + 2)):
        if y == p[0]:
            continue
        res.append([y, p[1]])

    for x in range(max(0, p[1] - 1), min(len(s[0]), p[1] + 2)):
        if x == p[1]:
            continue
        res.append([p[0], x])

    return res


def find_connecting(maze, origin):
    res = []
    conn = get_surrounding(maze, origin)

    for i in conn:
        if get_realtive(origin, i) in joints[maze[i[0]][i[1]]]:
            res.append(i)

    return res


def get_other(s, lst):
    for x in lst:
        if s != x:
            return x


def parse_line(s):
    return [x for x in s]


def parse_maze(s):
    return [parse_line(x) for x in s.split("\n")]


def print_path(s, path):
    for y in range(len(s)):
        for x in range(len(s[0])):
            if [y, x] in path:
                print("\033[0;30;41m", s[y][x], end="", sep="")
            else:
                print("\033[0;30;40m", s[y][x], end="", sep="")
        print("\033[0;30;40m")
    print("\033[0;30;40m")


def get_inside_path(s, path):
    pass


def part_1(i):
    start = find_start(i)
    print(start)

    start_el = find_connecting(i, start)
    curr = start_el[0]
    last = get_realtive(start, curr)
    path = []
    while True:
        path.append(curr)

        next_rel = get_other(last, joints[i[curr[0]][curr[1]]])
        next = [curr[0] + next_rel[0], curr[1] + next_rel[1]]

        if i[next[0]][next[1]] == "S":
            break

        last = get_realtive(curr, next)
        curr = next

    return (len(path) + 1) / 2


def part_2(i):
    start = find_start(i)
    print(start)

    start_el = find_connecting(i, start)
    curr = start_el[0]
    last = get_realtive(start, curr)
    path = []
    while True:
        path.append(curr)

        next_rel = get_other(last, joints[i[curr[0]][curr[1]]])
        next = [curr[0] + next_rel[0], curr[1] + next_rel[1]]

        if i[next[0]][next[1]] == "S":
            break

        last = get_realtive(curr, next)
        curr = next

    print_path(i, path)


parsed_input = parse_maze(input)
print(parsed_input)

part_1_res = part_1(parsed_input)
print(part_1_res)

part_2_res = part_2(parsed_input)
print(part_2_res)
