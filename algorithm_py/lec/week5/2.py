### 과제2.

'''
두 문자열 A와 B가 있을 때, 두 문자열의 '최대공약문자열' C를 아래와 같이 정의하자.

문자열 C를 반복하여 문자열 A와 B를 생성할 수 있다.
가능한 C 중에 가장 긴 문자열을 C로 한다.
위 조건을 만족하는 C가 없으면 빈 문자열을 C로 한다.
이 때, 문자열 A와 B를 입력받아 C를 출력하는 프로그램을 작성하시오.
'''

'''
예시입력1
A = 'ababcde'
B = 'ababcde'
출력: 'ababcde'

예시입력2
A = 'ababababab'
B = 'abab'
출력: 'ab'

예시입력3
A = 'abababab'
B = 'abab'
출력: 'abab'

예시입력3
A = 'fast'
B = 'campus'
출력: ''
'''

# 내 풀이 ----------------------------------------------------------------------------

def gcdString(A, B):
    gcd = ""
    # 둘 중 최소값 기준으로 반복
    for i in range(1, min(len(A), len(B)) + 1):  
        # 반복되어야 되기 때문에 A, B 각각 최대공약문자열의 n배인지 확인      
        if len(A) % i == 0 and len(B) % i == 0:
            str1 = A[:i]
            a1 = len(A) // i
            b1 = len(B) // i

            # 몇배인지 확인후 중복문자 배수를 곱했을 때 둘다 같을 경우 반환  
            if str1 * a1 == A and str1 * b1 == B:
              gcd = str1

    return gcd  

# 예시입력 테스트
A = 'ababababab'
B = 'abab'
print(gcdString(A, B))    

# 강사님 풀이 ------------------------------------------------------------------------- 
#탐욕 알고리즘으로 적절한 답안을 찾아내는 문제였습니다.
#문제에서 제시하는 정의에 맞게 잘 구현해 주셨습니다 :)

def gcdString(A, B):
    def isDivisor(string, divisor):
        n = len(divisor)
        if len(string) % n != 0:
            return False
 
        while string != '':
            if string[:n] != divisor:
                return False
            string = string[n:]
        return True
 
    if len(A) > len(B):
        str1, str2 = A, B
    else:
        str1, str2 = B, A
 
    divisor = str2
    m = 1
    while divisor != '':
        if isDivisor(str2, divisor) and isDivisor(str1, divisor):
            return divisor
        m += 1
        divisor = str2[:len(str2) // m]
    return ''