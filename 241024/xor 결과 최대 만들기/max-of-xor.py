import sys

def choose_nums(i, idx, xor_nums):

    global result

    if i == m:
        xor = 0
        for x in xor_nums:
            xor ^= x
        if result == 0 or result < xor:
            result = xor
        return 

    if idx < n:
        xor_nums.append(nums[idx])
        choose_nums(i+1, idx+1, xor_nums)
        xor_nums.pop()
        choose_nums(i, idx+1, xor_nums)

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

result = 0
choose_nums(0, 0, [])
print(result)