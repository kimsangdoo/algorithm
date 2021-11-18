'''
'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.

만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.

만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
'''

'''
입력
보드의 크기 N (2 ≤ N ≤ 100)
사과의 개수 K (0 ≤ K ≤ 100)
뱀의 방향 변환 횟수 L (1 ≤ L ≤ 100)
사과의 위치가 담긴 리스트 apples
첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
뱀의 방향 변환 정보 moves
정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

예시입력1
입력
N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]
출력: 9

예시입력2
입력
N = 10
K = 4
L = 4
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
출력: 21

예시입력3
입력
N = 10
K = 5
L = 4
apples = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
출력: 13
'''


'''
def solution(N, K, L, apples, moves):
    result = 0
    return result
 
N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]
print(solution(N, K, L, apples, moves))
 
N = 10
K = 4
L = 4
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))
 
N = 10
K = 5
L = 4
apples = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))
'''


from collections import deque

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

def solution(N, K, L, apples, moves):

    arr = [[0] * N for _ in range(N)]
    for i in range(K):
        a, b = apples[i][0], apples[i][1]
        arr[a - 1][b - 1] = 1  # 사과 저장
    
    times = {}
    for i in range(L):
        X, C = moves[i][0], moves[i][1]
        times[int(X)] = C    

    direction = 1  # 초기 방향
    time = 1  # 시간
    y, x = 0, 0  # 초기 뱀 위치
    visited = deque([[y, x]])  # 방문 위치
    arr[y][x] = 2

    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1:  # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                arr[temp_y][temp_x] = 0  # 꼬리 제거
            arr[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time




 
N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]
print(solution(N, K, L, apples, moves))
 
N = 10
K = 4
L = 4
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))
 
N = 10
K = 5
L = 4
apples = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))