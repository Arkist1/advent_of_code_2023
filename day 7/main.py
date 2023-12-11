from string import ascii_letters

input = open("input.txt", "r").read()

print(input)


def parse_bid(s):
    return int(s)


def parse_hand(s):
    return [x for x in s]


def parse_line(s):
    return [parse_hand(s.split(" ")[0]), parse_bid(s.split(" ")[1])]


def parse_lines(s):
    return [parse_line(x) for x in s.split("\n")]


def freq(s):
    res = {}
    for x in s:
        if x in res.keys():
            res[x] += 1
        else:
            res[x] = 1

    return res


def kind5(s, j, max_card):
    return True if max(s) + j == 5 or j > 4 else False


def kind4(s, j, max_card):
    return True if max(s) == 4 or max(s) + j == 4 or j >= 3 else False


def kind3(s, j, max_card):
    return True if max(s) == 3 or max(s) + j == 3 or j >= 2 else False


def kind2(s, j, max_card):
    return True if max(s) == 2 or max(s) + j == 2 or j >= 1 else False


def kind1(s, j, max_card):
    return True if max(s) == 1 else False


def full_house(s, j, max_card):
    return True if len(s) == 2 else False


def pair2(s, j, max_card):
    return True if max(s) == 2 and len(s) == 3 or max(s) == 1 and j == 2 else False


score = "AKQT98765432J"
hand_types = [kind5, kind4, full_house, kind3, pair2, kind2, kind1]


def get_all_non_j(s):
    if len(s) == 1:
        return s
    res = {}
    for x in s.items():
        if x[0] != "J":
            res[x[0]] = x[1]

    return res


def get_type(s, hand_types=hand_types):
    s_freq = freq(s)
    for x in hand_types:
        if x(
            get_all_non_j(s_freq).values(),
            s_freq.get("J", 0),
            sorted(s_freq.items(), key=lambda x: x[1])[-1][0],
        ):
            return x


def hash(s):
    res = [list(reversed(hand_types)).index(s[2])]
    for x in s[0]:
        res.append(list(reversed(score)).index(x))
    return res


def part_1(i):
    for index, x in enumerate(i):
        i[index].append(get_type(x[0]))

    res = []
    for index, val in enumerate(
        sorted(i, key=lambda x: [ascii_letters[y] for y in hash(x)])
    ):
        print(val, index)
        res.append(val[1] * (index + 1))

    return res


def part_2(i):
    pass


parsed_input = parse_lines(input)
print(parsed_input)

part_1_res = part_1(parsed_input)
print(sum(part_1_res))


251137389
251137389
251001655
251031935
251277844
251429090
