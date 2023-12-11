import string

input = open("input.txt", "r").read()


def parse_section(s):
    s = s.split("\n")
    title = s[0].split(" ")[0].strip().split("-")

    res = []
    for x in s[1:]:
        res.append([int(y) for y in x.strip().split(" ")])

    return ((title[0], title[2]), res)


def parse_file(f):
    sections = f.split("\n\n")
    res = {"seeds": [int(x) for x in sections[0].split(":")[1].strip().split(" ")]}
    res["sections"] = {}
    for x in sections[1:]:
        p = parse_section(x)
        res["sections"][p[0]] = p[1]

    return res


def get_ranges(seeds):
    res = []
    for index in range(0, len(seeds), 2):
        res.append([seeds[index], seeds[index] + seeds[index + 1]])
    return res


def sort_ranges(ranges):
    return list(sorted(ranges, key=lambda x: x[0]))


def part_1(i):
    res = {}
    res["seed"] = i["seeds"]
    for index, x in i["sections"].items():
        ranges = [[y[1], y[1] + y[2], y[0] - y[1]] for y in x]
        res[index[1]] = []

        # print(ranges)
        for s_index, s in enumerate(res[index[0]]):
            for r in ranges:
                if r[0] <= s < r[1]:
                    res[index[1]].append(s + r[2])
                    break

            if len(res[index[1]]) != s_index + 1:
                res[index[1]].append(s)

        # print(f"{res[index[0]]} -> {res[index[1]]}")
        # print()
    return res


def part_2(i):
    res = {}
    res["seed"] = get_ranges(i["seeds"])
    for index, x in i["sections"].items():
        ranges = [[y[1], y[1] + y[2], y[0] - y[1]] for y in x]
        res[index[1]] = []

        for s_index, s in enumerate(res[index[0]]):
            res_ranges = []
            for r in ranges:
                if s[0] <= r[0] <= s[1] and s[0] <= r[1] <= s[1]:
                    res_ranges.append(r)
                    continue

                if s[0] >= r[0] and r[1] >= s[1]:
                    res_ranges.append([s[0], s[1], r[2]])
                    continue

                if s[0] <= r[0] < s[1]:
                    res_ranges.append([r[0], s[1], r[2]])
                    continue

                if s[0] <= r[1] < s[1]:
                    res_ranges.append([s[0], r[1], r[2]])
                    continue

            if len(res_ranges) == 0:
                res_ranges.append([s[0], s[1], 0])

            s_ranges = sort_ranges(res_ranges)

            # check first range
            if s_ranges[0][0] != s[0]:
                s_ranges.insert(0, [s[0], s_ranges[0][0], 0])

            # check last range
            if s_ranges[-1][1] != s[1]:
                s_ranges.append([s_ranges[-1][1], s[1], 0])

            # check for missing ranges in the middle
            for x in range(0, len(sort_ranges(s_ranges)) - 1):
                if s_ranges[x][1] != s_ranges[x + 1][0]:
                    s_ranges.append([s_ranges[x][1], s_ranges[x + 1][0], 0])

            # applying delta's
            final_ranges = []
            for x in s_ranges:
                final_ranges.append([x[0] + x[2], x[1] + x[2]])

            # print(final_ranges)
            # print()
            for x in final_ranges:
                res[index[1]].append(x)

    return res


parsed_input = parse_file(input)
print(parsed_input)


part_1_res = part_1(parsed_input)
print(min(part_1_res["location"]))

part_2_res = part_2(parsed_input)
print(min(part_2_res["location"])[0])
