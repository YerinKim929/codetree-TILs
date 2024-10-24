def is_right(nums):
    k = len(nums)

    if k >= 2:
        for start in range(0, k):
            for end in range(2, k+1, 2):
                if start+end <= k:
                    tmp = nums[start:start+end]
                    if tmp[:end//2] == tmp[end//2:]:
                        return 0

    return 1


def choose_nums(i, nums):
    global result
    
    if i == n:
        result.append("".join(map(str,nums)))
        return 

    nums.append(4)
    if is_right(nums):
        choose_nums(i+1, nums)
    nums.pop()

    nums.append(5)
    if is_right(nums):
        choose_nums(i+1, nums)
    nums.pop()

    nums.append(6)
    if is_right(nums):
        choose_nums(i+1, nums)
    nums.pop()
    

n = int(input())

result = []
choose_nums(0, [])
print(result[0])