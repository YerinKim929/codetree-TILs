import sys
from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(cur, cmd):
    # 1-2: 최단거리 이동, 상 좌 우 하 우선순위 (도달하기까지 거쳐야하는 칸의 수가 최소되는 거리)
    # 3-1에서도 사용

    dxs = [-1, 0, 0, 1]
    dys = [0, -1, 1, 0]
    visited = [[0]*n for _ in range(n)]
    footprint = [[0]*n for _ in range(n)]

    q = deque([cur])
    visited[cur[0]][cur[1]] = -1

    distance = 99999999
    destination = []

    while q:
        now = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = now[0]+dx, now[1]+dy
            if in_range(new_x, new_y) and board[new_x][new_y] >= 0 and not visited[new_x][new_y]:
                if visited[now[0]][now[1]] == -1:
                    visited[new_x][new_y] = 1
                else:
                    visited[new_x][new_y] = visited[now[0]][now[1]] + 1
                q.append([new_x, new_y])
                # 3-2: 가장 가까운(최단거리) 베이스캠프 여러개면 행이 작은, 열이 작은 베이스 캠프로 들어감 
                if cmd == "basecamp":
                    if board[new_x][new_y] == 1 and distance >= visited[new_x][new_y]:
                        if distance == visited[new_x][new_y]:
                            if destination[0] > new_x or (destination[0] == new_x and destination[1] > new_y):
                                distance = visited[new_x][new_y]
                                destination = [new_x, new_y]
                        else:
                            distance = visited[new_x][new_y]
                            destination = [new_x, new_y]
                else:
                    footprint[new_x][new_y] = now
                    destination = footprint
                            
    return destination

def move_to__store(i):
    person = people[i]
    dest = stores[i]
    footprint = bfs(person, dest)

    cur =  footprint[dest[0]][dest[1]]
    moving = [cur]

    while cur != person:
        cur = footprint[cur[0]][cur[1]]
        moving.append(cur)

    if len(moving) > 1:
        people[i] = moving[-2]
    else:
        people[i] = dest

        # 2-1: 편의점 도착시 편의점에서 멈춤 
        finish[i] = 1
        return dest
      
    return []




def fine_close_basecamp(i):
    store = stores[i]
    basecamp = bfs(store, "basecamp")
    # 3-3: t번 사람이 베이스 캠프로 이동하는데에 시간 소요 안됨 
    people.append(basecamp)
    # 3-4: 이때부터 다른 사람들은 해당 베이스캠프 있는 칸 못지나감
    # 3-5: t번 사람이 편의점 향해 움직이기 시작해도 해당 베이스캠프 앞으로 절대 지나갈 수 없음 
    # 3-6: 마찬가지로 해당 턴 격자에 있는 사람들이 모두 이동한 뒤 해당 칸 지나갈 수 없어짐 
    board[basecamp[0]][basecamp[1]] = -1



# 빵 구학자 하는 m명의 사람, m번 사람은 정확히 m분에 각자 베이스캠프에서 출발해 편의점 이동
# 출발 시간 되기 전까지 격자 밖, 목표 편의점 모두 다름 

# n*n크리 격자 위
n, m = map(int, sys.stdin.readline().split())
# 격자 0: 빈공간, 1: 베이스캠프
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
# 사람들 가고 싶어하는 편의점 위치 (겹치지 X)
stores = []
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    stores.append([x-1, y-1])
# 격자 안 사람들 위치 
people = []
finish = [0]*m

t = 0
while sum(finish) < m:
    # 1~3가지 행동은 총 1분동안 진행, 정확히 1, 2, 3 순서로 진행
    no_move = []
    for i in range(len(people)):
        # 1, 2번 진행
        # 1-1: 격자에 있는 사람들 모두가 본인 가고 싶은 편의점 방향 향해 1칸 이동
        if not finish[i]:
            dest = move_to__store(i)
            # 2-2: 이때 다른 사람들은 해당 편의점 있는 칸 지나갈 수 없음 
            if dest:
                no_move.append(dest)
    
    # 2-3: 근데 격자에 있는 사람 모두가 이동한 뒤에 해당 칸을 지나갈 수 없어 짐 
    for no in no_move:
        board[no[0]][no[1]] = -1

    # 3번  진행 
    # 3-1: 현재 시간 t분이고 t<=m 만족시 t번 사람은 자신이 가고 싶은 편의점과 가장 가까운 베이스캠프에 들어감
    if t < m:
        fine_close_basecamp(t)

    t += 1

print(t)