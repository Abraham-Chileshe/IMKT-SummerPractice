import sys
from collections import defaultdict

line = sys.stdin.readline().replace("\n", "")
words = defaultdict(int)

while line:
    for word in line.split():
        words[word] += 1
    line = sys.stdin.readline().replace("\n", "")

print("\n".join(dict(sorted(words.items(), key=lambda x: (-x[1], x[0]))).keys()))
