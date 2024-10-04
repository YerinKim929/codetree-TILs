import sys 

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_player(p, action):
    player = players[p]

    # d에 알맞게 배열 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    nxt_x = player[0] + dx[player[2]]
    nxt_y = player[1] + dy[player[2]]

    # 그냥 초반에 움직일 때 
    if not action:
        if not in_range(nxt_x, nxt_y):
            # 정반대 방향으로 한칸 
            move_d = None
            if player[2] > 1:
                move_d = player[2]-2
            else:
                move_d = player[2]+2

            nxt_x = player[0] + dx[move_d]
            nxt_y = player[1] + dy[move_d]
            players[p][2] = move_d
    # 지고 나서 한칸 더 움직일 때 
    else:
        # 만약 플레이어가 있거나 격자 밖으로 벗어나면 오른쪽으로 90도 회전하고 빈칸이 보이면 순간이동 
        for i in range(4):
            new_d = player[2] + i if player[2] + i < 4 else player[2] + i - 4
            nxt_x = player[0] + dx[new_d]
            nxt_y = player[1] + dy[new_d]
            if check_player(p, [nxt_x, nxt_y]) == -1 and in_range(nxt_x, nxt_y):
                players[p][2] = new_d
                break


    # 변환된 위치 플레이어에 입력
    players[p][0:2] = [nxt_x, nxt_y]

    if action:
        choose_gun(p)

def check_player(p, position):
    is_player = -1
    for i in range(m):
        if p != i and position == players[i][0:2]:
            is_player = i
            break
    return is_player

    
def check_board(p):
    player = players[p]
    # 일단 이동 위치에 플레이어가 있는지 확인
    is_player = check_player(p, player[0:2])
    if is_player != -1:
        # 플레이어를 만나면 싸운다. 
        attack(p, is_player)
    # 플레이어를 만나지 않고, 건총이 있으면 총 고름
    if board[player[0]][player[1]] > 0:
        choose_gun(p)


# 플레이어1이 이동한 사람 번호, 플레이어2가 원래 있던 사람 번호
def attack(p1, p2):
    player1_power = players[p1][3] + guns[p1]
    player2_power = players[p2][3] + guns[p2]

    # 각자 싸우고 점수 계산 올리기 
    winer_p = p1
    point = abs(player1_power - player2_power)
    if player1_power > player2_power:
        points[p1] += point
    elif player1_power < player2_power:
        winer_p = p2
        points[p2] += point
    else:
        if players[p1][3] > players[p2][3]:
            points[p1] += point
        else:
            winer_p = p2
            points[p2] += point

    loser_p = p1 if winer_p == p2 else p2
    # 이기고 지고에 따라 또 뭐가 달라짐 
    lose_action(loser_p)
    # 이기면 총 고르기 
    choose_gun(winer_p)

def choose_gun(p):
    player = players[p]
    # 바닥의 총이 더 쎄면 원래 꺼 내려놓고 주움
    # 격자에 있는 총이 더 쎔
    if guns[p] < board[player[0]][player[1]]:
        gun = board[player[0]][player[1]] 
        # 그리고 예비 총보다 원래 총이 더 쎔 
        if guns[p] > pre_guns[player[0]][player[1]]:
            board[player[0]][player[1]] = guns[p]
        else:
            board[player[0]][player[1]] = pre_guns[player[0]][player[1]]
            pre_guns[player[0]][player[1]] = guns[p]
        guns[p] = gun



def lose_action(loser_p):

    loser = players[loser_p]
    # 총 격자에 내려놓기 
    tmp = board[loser[0]][loser[1]]
    # 격자보다 원래 총이 더 쎔
    if board[loser[0]][loser[1]] < guns[loser_p]:
        board[loser[0]][loser[1]] = guns[loser_p]
        pre_guns[loser[0]][loser[1]] = tmp
    else:
        pre_guns[loser[0]][loser[1]] = guns[loser_p]

    guns[loser_p] = 0
    # 원래 가려고 했던 방향대로 한 칸 이동 
    move_player(loser_p, 1)


# n: 격자의 크기, m: 플레이어의 수, k: 라운드 수 
n, m, k = map(int, sys.stdin.readline().split())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
players = []
# 플레이어 정보, x, y, d(방향), s(초기 능력치)
for _ in range(m):
    x, y, d, s = map(int, sys.stdin.readline().split())
    players.append([x-1, y-1, d, s])

# 플레이어가 최종적으로 얻는 포인트
points = [0]*m
# 현재 가지고 있는 총
guns = [0]*m
pre_guns = [[0]*n for _ in range(n)]

for i in range(k):
    for p in range(m):
        # 플레이어 이동 
        move_player(p, 0)
        # 격자 확인
        check_board(p)
        
for point in points:
    print(point, end=" ")