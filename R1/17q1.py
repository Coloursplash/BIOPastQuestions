# printed the whole triangle instead of just the last line
# i'm a chad, 110%

line_one = input()
triangle = [[x for x in line_one]]


def gen_letter(letter_one, letter_two):
    letters = ["R", "B", "G"]
    if letter_one == letter_two:
        return letter_one
    else:
        letters.remove(letter_one)
        letters.remove(letter_two)
        return "".join(letters)


while len(triangle[-1]) > 1:
    new_line = []
    for i in range(len(triangle[-1]) - 1):
        new_line += gen_letter(triangle[-1][i], triangle[-1][i + 1])
    triangle.append(new_line)

padding = 0

for line in triangle:
    print((" " * padding) + " ".join(line))
    padding += 1
