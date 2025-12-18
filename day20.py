# make all the factors that go into N , then sum(N)*10
from collections import Counter

limit = 36000000


def part1():
    count = Counter()
    for i in range(1, limit // 10):
        for j in range(i, limit // 10, i):
            count[j] += i * 10

    print(min([k for k, v in count.items() if v >= limit]))


def part2():
    count = Counter()
    for i in range(1, limit // 11):
        counter = 0
        for j in range(i, limit // 11, i):
            count[j] += i * 11
            counter += 1
            if counter == 50:
                break
    print(min([k for k, v in count.items() if v >= limit]))

part1()
part2()
