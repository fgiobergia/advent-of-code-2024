
def is_valid(seq, i):
    return ((seq[i] > seq[i+1] and seq[0] > seq[1]) or (seq[i] < seq[i+1] and seq[0] < seq[1])) and 1 <= abs(seq[i+1]-seq[i]) <= 3

def is_valid_report(report):
    return all(is_valid(report, i) for i in range(len(report)-1))

def is_valid_robust(report):
    i = 0
    while i < len(report) -1:
        if not is_valid(report, i):
            return is_valid_report(report[:i] + report[i+1:]) or is_valid_report(report[:i+1] + report[i+2:])
        i += 1
    return True

with open("day02.input") as f:
    lines = [ list(map(int, line.split(" "))) for line in f ]
valid = sum([ is_valid_report(line) for line in lines ])
print(valid)
valid = sum([ is_valid_robust(line) for line in lines ])
print(valid)
