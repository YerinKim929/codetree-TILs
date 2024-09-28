import sys 

def is_in_first_box(start_r_2, end_r,start_c_2, end_c):
    return start_r_2 <= end_r and start_c_2 <= end_c

def calculate_sum(start_r, end_r, start_c, end_c):

    box_sum = 0

    for r in range(start_r, end_r+1):
        for c in range(start_c, end_c+1):
            box_sum += board[r][c]

    return box_sum

n, m = map(int, sys.stdin.readline().split())

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

max_sum = -99999
first_box = 0
second_box = 0

# 첫번째 박스 계산 
for start_r in range(n):
    for end_r in range(start_r, n):
        for start_c in range(m):
            for end_c in range(start_c, m):
                first_box = calculate_sum(start_r, end_r, start_c, end_c)
                
                # 두번째 박스 계산
                for start_r_2 in range(n):
                    for end_r_2 in range(start_r_2, n):
                        for start_c_2 in range(m):
                            for end_c_2 in range(start_c_2, m):
                                if is_in_first_box(start_r_2, end_r,start_c_2, end_c):
                                    break
                                
                                second_box = calculate_sum(start_r_2, end_r_2, start_c_2, end_c_2)

                                # 비교 
                                max_sum = max(max_sum, first_box+second_box)
                                
                


print(max_sum)