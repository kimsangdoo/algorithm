## 과제3.

'''
민수는 최근 숫자 세기 놀이에 푹 빠져있다. 민수는 숫자를 N진수로 세며, 9보다 큰 숫자는 한자리로 표현하기 위해 아래와 같이 바꾸어서 센다.

10 ~ 35: a~z (알파벳 소문자)
36 ~ 61: A~Z (알파벳 대문자)
민수가 N진수의 숫자를 start부터 end까지 센 결과를 counts라고 할 때, 민수가 잘 못 센 숫자의 개수를 반환하는 함수를 구현하시오.

(단, 2 < N <= 62, start < end이며, counts의 길이는 (end - start + 1)이다.)
'''

'''
입출력 예시
N	    start	    end       	counts        	        return
14	  '9'	      'd'	  ['9', 'a', 'c', 'd', 'e']	      3
62	  'Z'	      '12'	['Z', '10', '11', '12']	        0 
'''

'''
def solution(N, start, end, counts):
    answer = 0
    return answer
'''

# 내 풀이 ----------------------------------------------------------------------------
def solution(N, start, end, counts):
    answer = 0
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    
    idx1 = 0
    for j in range(len(start)):
        idx1 += arr.index(start[j:j+1]) * (N**(len(start)-j-1))
    
    for i in range(0, len(counts)):     
        idx2 = 0
        
        for k in range(len(counts[i])):
            idx2 += arr.index(counts[i][k:k+1]) * (N**(len(counts[i])-k-1))
        
        if idx1 + i == idx2:
            pass
        else:
            answer+=1
    
    return answer


# 테스트 코드
#N, start, end, counts = 14,	'9',	'd',	['9', 'a', 'c', 'd', 'e']       # 3
N, start, end, counts = 62,	'Z',	'12',	['Z', '10', '11', '12']         # 0
solution(N, start, end, counts)

# 강사님 풀이 ------------------------------------------------------------------------- 
#조건에 맞는 진수법을 구현하는 문제였습니다.
#딕셔너리를 이용하면 비교적 간단하게 구현이 가능합니다.
#아래 예시 답안을 확인해주세요!

def solution(N, start, end, counts):
    mapper = {
        str(x):x for x in range(10)
    }
 
    offset = len(mapper)
    mapper.update({
        chr(x):x - ord('a') + offset for x in range(ord('a'), ord('z') + 1)
    })
 
    offset = len(mapper)
    mapper.update({
        chr(x):x - ord('A') + offset for x in range(ord('A'), ord('Z') + 1)
    })
 
    def todec(s):
        val = 0
        for i, n in enumerate(s[::-1]):
            val += mapper[n] * N**i
        return val
 
    answer = 0
 
    start = todec(start)
    end = todec(end)
    for s, target in zip(counts, range(start, end + 1)):
        print(todec(s))
        if todec(s) != target:
            answer += 1
 
    return answer
 
 
N = 13
start = '9'
end = 'd'
counts = ['9', 'a', 'c', 'd', 'e']
print(solution(N, start, end, counts))
 
N = 62
start = 'Z'
end = '12'
counts = ['Z', '10', '11', '12'] 
print(solution(N, start, end, counts))