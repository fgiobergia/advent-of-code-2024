import re

def mul(seq):
    return sum([ int(m[0]) * int(m[1]) for m in re.findall("mul\((\d{1,3}),(\d{1,3})\)", seq) ])

with open("day03.input") as f:
    seq = f.read().strip().replace("\n", "")

print(mul(seq))

seq = re.sub("don't\(\).*?do?\(\)", "", seq)
seq = re.sub("don't\(\)(?!.*do\(\)).*", "", seq)
print(mul(seq))