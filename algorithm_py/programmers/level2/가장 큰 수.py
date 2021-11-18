### 과제1.

'''
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
'''

'''
제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
'''

'''
입출력 예
        numbers	                return
      [6, 10, 2]	               6210
  [3, 30, 34, 5, 9]	            9534330
'''

'''
def solution(numbers):
    answer = 0
    return answer
'''

# 내 풀이 ----------------------------------------------------------------------------

def solution(numbers):

    num_str = [str(num) for num in numbers]

    num_str.sort(key = lambda x: (x*4)[:4], reverse = True)

    if num_str[0] != "0":
        answer = "".join(num_str)
        return answer
    else:
        return "0"


# 테스트
numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]

#solution(numbers1)
solution(numbers2)

# 강사님 풀이 ------------------------------------------------------------------------- 
#재귀적으로 구현하면 비교적 쉽게 구현할 수 있는 구현 문제였습니다.
#요구사항에 맞게 잘 구현해 주셨습니다! :) 아래 예시 답안도 확인해 주세요 :)

def solution(intervals):
    intervals.sort()
 
    def merge(x):
        if len(x) <= 1:
            return x
 
        to_merge = [x[0]]
        del x[0]
        while len(x) > 0:
            if to_merge[0][1] >= x[0][0]:
                to_merge.append(x[0])
                del x[0]
            else:
                break
 
        merged = [to_merge[0][0], max(map(lambda e: e[1], to_merge))]
        return [merged] + merge(x)
 
    return merge(intervals)
 
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution(intervals))
 
intervals = [[1,4],[4,5]]
print(solution(intervals))