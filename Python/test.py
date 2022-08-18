import sys
input = sys.stdin.readline
m = 10001
l = [0]*m
for _ in range(int(input())):
    l[int(input())] += 1
for i in range(1, m):
    print(f"{i}\n"*l[i], end="")
