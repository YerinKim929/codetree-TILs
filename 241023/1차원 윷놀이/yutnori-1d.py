import sys
import copy

def choose(i, goal):
    global answer 

    if i == n:
        tmp = 0
        for g in goal:
            if g >= m:
                tmp += 1
        answer = max(answer, tmp)
        return 

    for j in range(0, k):
        copy_goal = copy.deepcopy(goal)
        copy_goal[j] += nums[i]
        choose(i+1, copy_goal)

n, m, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
answer = 0

choose(0, [1]*n)
print(answer)