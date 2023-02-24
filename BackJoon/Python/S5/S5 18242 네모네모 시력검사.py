import sys

n, m = list(map(int, sys.stdin.readline().split()))                 # 높이 n, 너비 m
board = [list(sys.stdin.readline().strip()) for _ in range(n)]      # 문자열 선언

def get_color(board):
    move = None

    for x in range(n):
        for y in range(m):
            if board[x][y] == '#':
                move = [x, y]
                break
        if move is not None:
            break

    return move

def get_width_height(board, nx, ny):
    right_t, left_b = [], []

    # 오른쪽 상단 모서리
    for y in range(m-1, ny, -1):
        if board[nx][y] == '#':
            right_t = [nx, y]
            break

    # 왼쪽 하단 모서리
    for x in range(n-1, nx, -1):
        if board[x][ny] == '#':
            left_b = [x, ny]
            break

    width = right_t[1] - ny + 1
    height = left_b[1] - nx + 1

    return width, height

# 사각형의 각 변 검사
def inspect(board, width, height, nx, ny):
    # UP, DOWN
    for y in range(ny, ny + width):
        if board[nx][y] == '.':
            return 'UP'
        if board[nx + height - 1][y] == '.':
            return 'DOWN'

    # LEFT, RIGHT
    for x in range(nx, nx + height):
        if board[x][ny] == '.':
            return 'LEFT'
        if board[x][ny + width - 1] == '.':
            return 'RIGHT'

def solution():
    move = get_color(board)
    width, height = get_width_height(board, *move)
    answer = inspect(board, width, height, *move)

    return answer

print(solution)