### 과제2.

'''
철수는 개발자에서 은퇴하여 치킨집을 하게 되었다. 철수는 뛰어난 개발 실력으로 N대의 자동 튀김기를 만들어냈다. i번째 자동 튀김기는 치킨을 한 번 튀기는 데에 fry[i] 만큼의 시간이 걸리며, 튀김이 한번 끝나면 clean[i] 만큼의 시간동안 자동 세척을 한다.

철수가 C 번 치킨을 튀겨내려고 할 때, 최소한 몇 시간 동안 자동 튀김기를 가동해야 하는지 계산하시오.
'''

'''
제약 사항
0 < N <= 100000
fry[i]는 0 < fry[i] <= 100를 만족하는 정수
clean[i]는 0 < clean[i] <= 100를 만족하는 정수
0 < C <= 100000
'''

'''
입출력 예
N	         fry	          clean	         C	          return
2	        [3, 6]        	[2, 1]	       20	            58
4	     [2, 2, 1, 3]	   [2, 4, 3, 2]	      2	             2
'''

'''
def solution(N):
    answer = 0
    return answer
'''

# 내 풀이 ----------------------------------------------------------------------------

def solution(N, fry, clean, C):
    cnt = 0
    second = 0
    
    while cnt != C:
        second += 1
        for i in range(N):
            if cnt == C:
                break
            elif fry[i]<second:
                  if (second-fry[i]) % (fry[i]+clean[i]) == 0:
                    cnt += 1
            elif fry[i] == second:
                cnt += 1     
            else:
                continue                               
    
    return second


# 테스트코드
N, fry, clean, C = 2,	[3, 6],	[2, 1], 20    # 58
#N, fry, clean, C = 4,	[2, 2, 1, 3],	[2, 4, 3, 2],	2    # 2    
print(solution(N, fry, clean, C))

# 강사님 풀이 ------------------------------------------------------------------------- 
#이분 탐색을 이용하여 넓은 범위를 빠르게 탐색하는 문제입니다.
#특정 시간 안에 목표 달성이 가능한지 아닌지 여부를 구현한 후, 이분 탐색을 이용하면 됩니다.
#탐색 범위가 넓은 점이 고려되지 않아, 일부 감점이 있습니다.
#아래 예시 답안을 확인해 주세요 :)

def solution(N, fry, clean, C):
    left = 0
    right = C * max([x+y for x, y in zip(fry, clean)])
    answer = right
 
    while left <= right:
        mid = (left + right) // 2
 
        val = 0
        for f, c in zip(fry, clean):
            val += (mid + c) // (f + c)
 
        if val >= C:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1
 
    return answer
 
N = 2
fry = [3, 6]
clean = [2, 1]
C = 20
print(solution(N, fry, clean, C))
 
N = 4
fry = [2, 2, 1, 3]
clean = [2, 4, 3, 2]
C = 2
print(solution(N, fry, clean, C))