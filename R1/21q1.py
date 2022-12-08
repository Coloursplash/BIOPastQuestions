# error with the mark scheme, EBCDFA is a pat even though B comes before F idk

from math import ceil
from itertools import permutations


def is_pat(pat: str):
    if len(pat) == 1:
        return True

    left_pat = pat[:ceil(len(pat) / 2)]
    right_pat = pat[ceil(len(pat) / 2):]

    if (not is_pat(left_pat[::-1])) or (not is_pat(right_pat[::-1])):
        return False

    if min(left_pat) < max(right_pat):
        return False

    return True


def test(pat: str):
    return "YES" if is_pat(pat) else "NO"


# part A
user = input("-> ")
pat1, pat2 = user.split(" ")
print(test(pat1))
print(test(pat2))
print(test(pat1 + pat2))

# part B
abcd = "ABCD"
print("ABCD valid perms")
for i in permutations(abcd):
    if len(i) == 4:
        if test("".join(i)) == "YES":
            print("".join(i))
