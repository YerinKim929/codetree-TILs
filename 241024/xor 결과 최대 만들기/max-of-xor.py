import sys

def choose_nums(i, xor_nums):

    global result

    if i == m:
        xor = 0
        for x in xor_nums:
            xor ^= x
        if result == 0 or result < xor:
            result = xor
        return 

    for j in range(0, n):
        xor_nums.append(nums[j])
        choose_nums(i+1, xor_nums)
        xor_nums.pop()

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

result = 0
choose_nums(0, [])
print(result)