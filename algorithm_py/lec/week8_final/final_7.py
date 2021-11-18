### 과제7. 2019년 LINE 인턴 채용 코딩테스트 문제
# 참고1: https://wooogy-egg.tistory.com/33
# 참고2: https://deepwelloper.tistory.com/entry/LINE-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%83%81%EB%B0%98%EA%B8%B0-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%8C%8C%ED%97%A4%EC%B3%90%EB%B3%B4%EA%B8%B0(실제 라인 풀이)

'''
연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다. 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다. 게임이 끝나는데 걸리는 최소 시간을 구하시오.

조건

코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다. 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.
출력 형식

브라운이 코니를 잡을 수 있는 최소시간 N초를 표준 출력한다. 단 브라운이 코니를 잡지 못한 경우에는 -1을 출력한다.
'''

'''
예제 입력
C	    B	    출력
11	  2	     5

예제 설명
코니의 위치: 11 → 12 → 14 → 17 → 21 → 26
브라운의 위치: 2 → 3 → 6 → 12 → 13 → 26
브라운은 코니를 5초 만에 잡을 수 있다.

def solution(C, B):
    result = 0
    return result
 
print(solution(11, 2))
'''


from collections import deque

#c = 11
#b = 2
#def catch_me(cony_loc, brown_loc):
def solution(C, B):
    time = 0
    queue = deque()
    queue.append((B, 0)) # 브라운의 위치와 시간을 동시에 잡아주기 위함
    # 위치와 시간이 동시에 일치해야하지만 만났다고 할 수 있기에.
    visited = [{} for _ in range(200001)]
    # visited의 각 원소들은 각 시간 0초에 어느 곳을 갔는지 저장하기 위한 시간
    # visited[0] = { 2: True }, visited[1] = { 1:True, 3:True, 4:True} ...
    # 20만개의 딕셔너리를 배열에 넣음 [{}, {}, {}, ...]
    # visited[위치][시간]
    # visited[3] 에 5라는 키가 있냐? -> 3위치에 5초에 간적이 있나

    # 초기 위치는 2고 0초 이므로
    # 시간 0 1 -> visited[2] = { 0 : True }
    # 위치 2 1 -> visited[1] = { 1: True}
    #       3 -> visited[3] = { 1: True}
    #       4 -> visited[4] = { 1: True}

    # 시간이 2초일때 가능한 것은 다시
    # 시간 2 -> visited[2] = { 0 : True, 2: True }
    # 위치 0 -> visited[1] = { 1: True}
    #     2 -> visited[3] = { 1: True, 2: True}
    #     3 -> visited[4] = { 1: True, 2: True}
    #     4 -> visited[5] = { 2: True}
    #     5 -> visited[5] = { 6: True}
    #     6 -> visited[5] = { 8: True}
    #     8

    while C <= 200000:
        C += time #시간만큼 더해짐
        if time in visited[C]:
            return time
            # 이렇게 해준다면 이 시간대에 방문하게 된 것이므로 코니와 브라운이 만나게 된 시점을 알 수 있음

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()
            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
            # 모든 경우의 수 저장을 위한 각각 격우의 수 저장
        time += 1
    return -1
 
print(solution(11, 2))

 
