import sys

def choose(m, start, nums):

    if m == M:
        print(" ".join(map(str, nums)))
        return 

    for i in range(start, N+1):
        if not i in nums:
            nums.append(i)
            choose(m+1, i+1, nums)
            nums.pop()


N, M = map(int, sys.stdin.readline().split())
choose(0, 1, [])