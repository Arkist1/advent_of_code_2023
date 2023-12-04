input = open("input.txt", "r").read()

print(input)


def parse_half_card(half_card):
    return [t for t in half_card.strip().split(" ") if t]


def parse_card(card):
    return [
        parse_half_card(half_card)
        for half_card in card.split(":")[1].strip().split("|")
    ]


def parse_cards(cards):
    return [parse_card(card) for card in cards.split("\n")]


def get_score(n):
    return bool(n) * 2 ** (n - 1) if n > 0 else 0


def multiple_in(s, m):
    cnt = 0
    for i in m:
        if i == s:
            cnt += 1

    return cnt


def part_1(i):
    res = []

    for card in i:
        cnt = 0
        for t in card[1]:
            if t in card[0]:
                cnt += 1

        print(cnt, get_score(cnt))
        res.append(get_score(cnt))

    return res


def part_2(i):
    copies = [1] * len(i)

    cnts = []
    for index, card in enumerate(i):
        cnt = 0
        for t in card[1]:
            cnt += multiple_in(t, card[0])

        cnts.append(cnt)

        for copy in range(index + 1, min(len(i), index + cnt + 1)):
            copies[copy] += copies[index]

    return copies


parsed_input = parse_cards(input)

part_1_res = part_1(parsed_input)
print(part_1_res)
print(sum(part_1_res))


part_2_res = part_2(parsed_input)
print(part_2_res)
print(sum(part_2_res))
