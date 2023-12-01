input = open("input.txt", "r").read()
input = input.split("\n")
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits = [str(x) for x in digits]
digits = {x: x for x in digits}
str_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
all_digits = digits | str_digits
reversed_digits = {x[0][::-1]: x[1] for x in all_digits.items()}


def get_digit(sample, reversed=False, digits=all_digits):
    if reversed:
        sample = sample[::-1]
    pos = [[x, sample.index(x)] for x in digits if x in sample]
    low = pos[0]
    for x in pos[1:]:
        if x[1] < low[1]:
            low = x

    return digits[low[0]]


def part1(sample):
    first = get_digit(sample, reversed=False, digits=digits)
    last = get_digit(sample, reversed=True, digits=digits)

    return first[0] + last[0]


def part2(sample):
    first = get_digit(sample, reversed=False, digits=all_digits)
    last = get_digit(sample, reversed=True, digits=reversed_digits)
    return first[0] + last[0]


res = []
for x in input:
    res.append(int(part1(x)))
print(sum(res))


res = []
for x in input:
    res.append(int(part2(x)))
print(sum(res))
