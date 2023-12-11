input = open("input.txt", "r").read()

print(input)


def parse_line(s):
    return [int(x.strip()) for x in s.split(":")[1].strip().split("   ")]


def parse_lines(x):
    return [parse_line(s) for s in x.split("\n")]


def prod(x):
    res = 1
    for y in x:
        res *= y

    return res


def app_int(x):
    res = ""
    for x in x:
        res += str(x)

    return int(res)


def part_1(i):
    pos = 1
    for d, t in zip(i[0], i[1]):
        game_pos = 0
        for i in range(0, d):
            if i * (d - i) > t:
                game_pos += 1

        pos *= game_pos

    return pos


def part_2(i):
    dist = app_int(i[0])
    target = app_int(i[1])
    print(dist, target)

    for i in range(0, dist):
        if i * (dist - i) > target:
            bottom = i
            break

    for i in range(dist, 0, -1):
        if i * (dist - i) > target:
            top = i
            break

    print(top, bottom)
    return top - bottom + 1


parsed_input = parse_lines(input)
print(parsed_input)

part_1_res = part_1(parsed_input)
print(part_1_res)


part_2_res = part_2(parsed_input)
print(part_2_res)
