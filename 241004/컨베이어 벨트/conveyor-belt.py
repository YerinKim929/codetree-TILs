import sys

n, t = map(int, sys.stdin.readline().split())
container1 = list(map(int, sys.stdin.readline().split()))
container2 = list(map(int, sys.stdin.readline().split()))
container = container1 + container2

for i in range(t):
    temp = container[2*n-1]
    for j in range(2*n-1, 0, -1):
        container[j] = container[j-1]
    container[0] = temp

for i in range(2*n):
    print(container[i], end=" ")
    if i == n-1:
        print()