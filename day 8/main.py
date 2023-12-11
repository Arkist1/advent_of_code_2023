from math import lcm


input = open("input.txt", "r").read()

print(input)

directions = {"L": 0, "R": 1}


def parse_directions(s):
    return [directions[x] for x in s]


def parse_output_node(s):
    return [x.strip(")").strip("(").strip() for x in s.split(", ")]


def parse_nodes(s):
    return {
        x.split(" = ")[0]: parse_output_node(x.split(" = ")[1]) for x in s.split("\n")
    }


def parse_lines(x):
    res = {}
    res["path"] = parse_nodes(x.split("\n\n")[1])
    res["directions"] = parse_directions(x.split("\n\n")[0])

    return res


def get_starting_nodes(nodes):
    return [node for node in nodes if node[-1] == "A"]


def is_end(s):
    for x in s:
        if x[-1] != "Z":
            return False

    return True


def part_1(i):
    curr = "AAA"
    j = 0

    while curr != "ZZZ":
        for instruction in i["directions"]:
            if curr == "ZZZ":
                break

            j += 1
            curr = i["path"][curr][instruction]

    return j


def part_2_sub(i, start, n_items=10):
    curr = start
    j = 0
    items = []

    while len(items) < n_items:
        for instruction in i["directions"]:
            if curr[-1] == "Z":
                items.append(j)

            j += 1
            curr = i["path"][curr][instruction]

    return items


def part_2(i):
    curr = get_starting_nodes(i["path"].keys())
    j = 0
    while not is_end(curr):
        for instruction in i["directions"]:
            print(j) if j % 100_000 == 0 else None

            if is_end(curr):
                print("DADISJIJ")
                break

            j += 1
            new_curr = []
            for index, x in enumerate(curr):
                new_curr.append(i["path"][x][instruction])

            curr = new_curr

    return j


parsed_input = parse_lines(input)
print(parsed_input)

# part_1_res = part_1(parsed_input)
# print(part_1_res)
res = {}
for x in get_starting_nodes(parsed_input["path"]):
    res[x] = part_2_sub(parsed_input, x, 1)

print(list(zip(*res.values())))
print(lcm(*(list(zip(*res.values()))[0])))

# part_2_res = part_2(parsed_input)
# print(part_2_res)
