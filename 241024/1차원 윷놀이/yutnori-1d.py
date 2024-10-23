import sys
import copy

# i = 턴수 / goal = 말의 위치
def choose(i, goal):
    global answer 

    if i == n:
        tmp = 0
        for g in goal:
            if g >= m:
                tmp += 1
        answer = max(answer, tmp)
        return 

    # 각 말마다 한턴씩 부여해서 주는 거지...
    for j in range(0, k):
        if goal[j] < m:
            copy_goal = copy.deepcopy(goal)
            copy_goal[j] += nums[i]
            choose(i+1, copy_goal)
        else:
            choose(n, goal)

n, m, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
answer = 0

choose(0, [1]*k)
print(answer)