import sys

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(cur_num):
    if cur_num == N + 1:
        print_answer()
        return

    for i in range(1, K+1):
        answer.append(i)
        choose(cur_num+1)
        answer.pop()

    return 




K, N = map(int, sys.stdin.readline().split())
answer = []

choose(1)