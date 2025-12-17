letters = "abcdefghijklmnopqrstuvwxyz"


def checksum(x) -> bool:
    if "i" in x or "o" in x or "l" in x:
        return False

    straight = False
    for a, b, c in zip(x, x[1:], x[2:]):
        if ord(a) < ord(b) < ord(c) and ord(b) - ord(a) == 1 and ord(c) - ord(b) == 1:
            straight = True

    if not straight:
        return False

    pairs = False
    pairpos: list[int] = []
    for i, (a, b) in enumerate(zip(x, x[1:])):
        if a == b:
            pairpos.append(i)

    all_pairs = all([y - x > 1 for x, y in zip(pairpos, pairpos[1:])])
    if len(pairpos) >= 2 and all_pairs:
        pairs = True
    else:
        return False

    return True


def incr(x: str) -> str:
    out = ""
    carry = 1
    tmp = ""
    for i, p in enumerate(x):
        if p == "i":
            tmp += "j"
            break
        elif p == "l":
            tmp += "m"
            break
        elif p == "o":
            tmp += "p"
            break
        else:
            tmp += p
    tmp += "a" * len(x[i + 1 :])

    for c in tmp[::-1]:
        n: int = letters.index(c) + carry
        carry: int = n // len(letters)
        out += letters[n % len(letters)]

    return out[::-1]


def next_pass(sp: str) -> str:
    # turn starting password into a number, so we just loop it.
    while True:
        sp: str = incr(sp)
        if checksum(sp):
            return sp


assert checksum("hijklmmn") is False
assert checksum("abbceffg") is False
assert checksum("abbcegjk") is False
assert checksum("abcdffaa") is True
assert checksum("ghjaabcc") is True

assert next_pass("abcdefgh") == "abcdffaa"
assert next_pass("ghijklmn") == "ghjaabcc"

p1 = next_pass("hxbxwxba")
print(p1)
p2 = next_pass(p1)
print(p2)
