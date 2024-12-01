from collections import Counter

with open("day01.input") as f:
    col1, col2 = zip(*[ list(map(int, x.split("   "))) for x in f ])

    print(sum([ abs(a-b) for a, b in zip(sorted(col1), sorted(col2)) ]))

    counts = Counter(col2)
    print(sum([ a * counts[a] for a in col1 ]))
