input = open("input.txt", "r").read()

print(input)


def parse_set(s):
    res = {}
    for x in s.split(","):
        x = x.strip().split(" ")
        res[x[1]] = int(x[0])

    return res
    return [
        {x.strip().split(" ")[1]: x.strip().split(" ")[0]} for x in s.strip().split(",")
    ]


def parse_game(g):
    return [parse_set(x.strip()) for x in g.split(";")]


def parse_input(i):
    return {
        x[5 : x.index(":")]: parse_game(x[x.index(":") + 1 :].strip())
        for x in i.split("\n")
    }


def get_power(args):
    res = 1
    for x in args:
        res = res * x

    return res


def part_1(parsed_input, max_bag):
    pos = []
    for index, game in parsed_input.items():
        breaked = False
        for set in game:
            for colour, amt in max_bag.items():
                if colour in set:
                    if set[colour] > amt:
                        breaked = True
                        break

        if not breaked:
            pos.append(int(index))

    return pos


def part_2(parsed_input):
    pow = []
    for index, game in parsed_input.items():
        max_clr = {}
        for set in game:
            for colour, amt in set.items():
                if not colour in max_clr.keys():
                    max_clr[colour] = amt
                else:
                    if max_clr[colour] < amt:
                        max_clr[colour] = amt

        pow.append(get_power(max_clr.values()))

    return pow


parsed_input = parse_input(input)
bag = {"red": 12, "green": 13, "blue": 14}

print(parsed_input)

part_1_res = part_1(parsed_input, bag)
print(sum(part_1_res))


part_2_res = part_2(parsed_input)
print(sum(part_2_res))
