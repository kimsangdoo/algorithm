### 과제3.

'''
N개의 문자열로 이루어진 List에서 전체 문자열이 앞 n개 문자열이 같다고 할때, 가장 큰 n을 출력하는 알고리즘을 구현하라. (즉, 주어진 모든 문자열의 앞의 몇개의 문자가 일치하는지 출력하라)

def solution(a):
    return 0
 
# Test code
print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) # 출력: 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 출력: 0
'''


# 내 풀이 ----------------------------------------------------------------------------
def solution(a):    
    # 변수 선언 : 카운트 집계, 플래그
    cnt = 0         
    flag = True

    # 문제에서 문자열 제한 없음, 불가능한 수로 최초 설정 : 1000000, 어차피 조건 안맞으면 바로 break
    for i in range(1000000):                
        for j in range(len(a)-1):
            # 조건 : 문자열 앞뒤가 같거나 + 예외추가(문자열이 끝나서 공백이 나오는 경우 걸러내기, 둘다 공백이 아닐때에만 실행가능하도록)
            if a[j][i:i+1] == a[j+1][i:i+1] and a[j][i:i+1] != '' and a[j+1][i:i+1] != '':
                pass
            else:
                flag = False
                break
        # 전부 다 실행, 또는 else에서 break되서 내려온 후 flag 상태에 따라 cnt 증가 또는 증가 없이 break                
        if flag:            
            cnt += 1                    
        else:
            break            
    # 최종 cnt 반환            
    return cnt

# 강사님 풀이 ------------------------------------------------------------------------- 
#문자열 매칭을 다루는 문제였습니다!
#잘 구현해 주셨습니다. 아래 예시 답안도 확인해 주세요! :)

def solution(a):
    count = 0
    w = a[0]
    for idx, c in enumerate(w):
        is_match = True
        for w_ in a:
            if c != w_[idx]:
                is_match = False
                break
        if is_match is True:
            count += 1
        else:
            break
    return count
