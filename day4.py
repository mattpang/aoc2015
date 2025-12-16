# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
from hashlib import md5


def find_md5(key: str, zeros: int = 5) -> int:
    num = 0
    while True:
        cand = key + str(num)
        cand_bytes = cand.encode("utf-8")
        out = md5(cand_bytes).hexdigest()
        if out.startswith("0" * zeros):
            return num
        num += 1
        # if num % 1000000 == 0:
        #     print(num)
    return None


# assert find_md5('abcdef') == 609043

print(find_md5("iwrupvqb", 5))
print(find_md5("iwrupvqb", 6))
