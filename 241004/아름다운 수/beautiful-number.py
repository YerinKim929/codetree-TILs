import sys

def is_beautiful(num):
    how = 0
    cur = 0
    for i in range(len(num)):
        if not cur or cur == num[i]:
            how += 1
        elif how % cur == 0:
            how = 1
        else:
            return 0

        cur = num[i]
    
    if how % cur != 0:
        return 0

    return 1

def num_beautiful(cur_n):
    global answer

    if cur_n == n+1:
        answer += is_beautiful(nums)
        return 
    
    for i in range(1, 5):
        nums.append(i)
        num_beautiful(cur_n+1)
        nums.pop()

    return

n = int(sys.stdin.readline())
answer = 0
nums = []
num_beautiful(1)
print(answer)