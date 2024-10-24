import sys

def choose_nums(i, xor_nums):

    global result

    if i == m:
        xor = None
        for x in xor_nums:
            if xor == None:
                xor = x
            else:
                xor ^= x
        if result == 0 or result < xor:
            result = xor
        return 

    for j in range(1, n+1):
        xor_nums.append(j)
        choose_nums(i+1, xor_nums)
        xor_nums.pop()

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

result = 0
choose_nums(0, [])
print(result)