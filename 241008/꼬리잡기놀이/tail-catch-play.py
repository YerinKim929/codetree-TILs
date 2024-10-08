import sys
from collections import deque

# n*n 격자에서 꼬리잡기 놀이 진행
# 3명 이상 한 팀
# 모든 사람은 자신 앞 사람 허리 잡고 움직이며, 맨 앞에 있는 사람 = 머리사람, 맨 뒤에 있는 사람 = 꼬리사람
# 각 팀은 게임에서 주어진 이동 선을 따라서만 이동
# 각 팀의 이동 선은 끝이 이어짐 
# 각 팀의 이동 선은 서로 겹치지 않음 
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_head(i):
    # 머리 사람 이동 
    head = heads[i]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = head[0] + dx, head[1] + dy

        if in_range(new_x, new_y):
            if board[new_x][new_y] == 4:
                board[new_x][new_y] = 1
                board[head[0]][head[1]] = 2
                heads[i] = [new_x, new_y]
            elif board[new_x][new_y] == 3:
                board[new_x][new_y] = 1
                heads[i] = [new_x, new_y]
                for dxx, dyy in zip(dxs, dys):
                    new_xx, new_yy = new_x+dxx, new_y+dyy
                    if in_range(new_xx, new_yy) and board[new_xx][new_yy] == 2:
                        board[new_xx][new_yy] = 3
                        tails[i] = [new_xx, new_yy]
                board[head[0]][head[1]] = 2
                return

    # 꼬리 사람 이동 
    if tails[i]:
        tail = tails[i]
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = tail[0] + dx, tail[1] + dy

            if in_range(new_x, new_y) and board[new_x][new_y] == 2:
                board[new_x][new_y] = 3
                board[tail[0]][tail[1]] = 4
                tails[i] = [new_x, new_y]
    else:

        q = deque([head])
        visited = [[0]*n for _ in range(n)]
        visited[head[0]][head[1]] = 1

        while q:

            cur = q.popleft()

            for dx, dy in zip(dxs, dys):
                new_x, new_y = cur[0] + dx, cur[1] + dy

                if in_range(new_x, new_y) and not visited[new_x][new_y]:
                    if board[new_x][new_y] == 2:
                        visited[new_x][new_y] = 1
                        q.append([new_x, new_y])
                    elif board[new_x][new_y] == 3:
                        board[new_x][new_y] = 4
                        board[cur[0]][cur[1]] = 3
                        tails[i] = cur
               
def throw_ball(rnd):

    # 2-3. 4n 번째 라운드 넘어가는 경우, 다시 1번째 라운드 방향으로 돌아감 
    if rnd > 4*n:
        rnd %= 4*n

    # 2-2. 우 (round 1 ~ n) 상 (round n + 1 ~ 2n) 좌 (round 3n ~ 2n + 1) 하 (round 4n ~ 3n + 1)   
    # return [r1, c1, r2, c2]
    if 1 <= rnd <= n:
        return [rnd-1, 0, rnd-1, n-1]
    elif n+1 <= rnd <= 2*n:
        rd = rnd-n
        return [n-1, rd-1, 0, rd-1]
    elif 2*n+1 <= rnd <= 3*n:
        rd = rnd-2*n
        return [n-rd, n-1, n-rd, 0]
    else:
        rd = rnd-3*n
        return [0, n-rd, n-1, n-rd]


def check_people(ball):

    start_r, end_r, direct_r = None, None, 1
    start_c, end_c, direct_c = None, None, 1

    if ball[0] <= ball[2]:
        start_r, end_r =  ball[0], ball[2]+1
    else:
        start_r, end_r = ball[0], ball[2]-1
        direct_r = -1

    if ball[1] <= ball[3]:
        start_c, end_c =  ball[1], ball[3]+1
    else:
        start_r, end_r = ball[1], ball[3]-1
        direct_c = -1

    for r in range(start_r, end_r, direct_r):
        for c in range(start_c, end_c, direct_c):
            if 0 < board[r][c] < 4:
                k = fine_k([r, c])
                return get_score(k)
    return 0

def fine_k(now):

    q = deque([now])
    visited = [[0]*n for _ in range(n)]
    visited[now[0]][now[1]] = -1

    if board[now[0]][now[1]] == 1:
        board[now[0]][now[1]] = 3
        i = heads.index(now)
        head = tails[i]
        board[head[0]][head[1]] = 1
        tails[i] = heads[i]
        heads[i] = head
        return 1

    while q:

        cur = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = cur[0] + dx, cur[1] + dy

            if in_range(new_x, new_y) and board[new_x][new_y] > 0 and not visited[new_x][new_y]:
                if visited[cur[0]][cur[1]] == -1:
                    visited[new_x][new_y] = 1
                else:
                    visited[new_x][new_y] = visited[cur[0]][cur[1]] + 1

                # 3-4. 공을 획득한 팀의 경우 머리사람과 꼬리사람이 바뀜 (방향 바뀜)
                if board[new_x][new_y] == 1:
                    board[new_x][new_y] = 3
                    i = heads.index([new_x, new_y])
                    head = tails[i]
                    board[head[0]][head[1]] = 1
                    tails[i] = heads[i]
                    heads[i] = head
                    return visited[new_x][new_y] + 1
                if board[new_x][new_y] != 3:
                    q.append([new_x, new_y])

    # 3-3. 아무도 공 받지 못하면 아무 점수도 획득 못함 
    return 0

# 3-2. 점수는 해당 사람이 머리 사람을 시작으로 팀 내 k번째 사람이라면 k의 제곱만큼 점수 얻음
def get_score(k):
    return k * k

# 격자의 크기 n, 팀의 개수 m, 라운드 수 k
n, m, k = map(int, sys.stdin.readline().split())
# 0 : 빈칸, 1 : 머리 사람, 2 : 그냥 사람, 3 : 꼬리 사람, 4 : 이동 선
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

heads = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            heads.append([r, c])
tails = [0]*m
total_score = 0


# 라운드 진행
for rnd in range(1, k+1):
    
    # 1. 먼저 각 팀은 머리 사람 따라서 한 칸 이동
    for i in range(m):
        move_head(i)

    # 2-1. 각 라운드마다 공이 정해진 선 따라 던져짐, n개의 행과 n개의 열 
    ball = throw_ball(rnd)

    # 3-1. 공이 던져지는 경우에 해당 선에 사람 있으면, 최초에 만나게 되는 사람만이 공을 얻어 점수 얻음
    total_score += check_people(ball)

print(total_score)