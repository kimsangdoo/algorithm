###과제4.

'''
반복문과 print() 함수를 이용하여 아래와 같은 출력을 하는 프로그램을 구현하시오.
'''

'''
출력:
0 1 2 4 8 16 32 64 128 256 256 256
'''



# 내 풀이 ----------------------------------------------------------------------------

# 1. i가 0일 때는 i 반환 / 2. 2의 i 제곱 256보다 커지는 경우는 256이 되도록 / 3, 나머지는 2의 i 제곱
str4 = ''
x = 8
for i in range(12):
    if(i == 0):        
        str4 += str(i) + ' '    
    else:
        if(i>x):
            str4 += str(2 ** (x)) + ' '
        else:           
            str4 += str(2 ** (i-1)) + ' '
print(str4)

# 강사님 풀이 ------------------------------------------------------------------------- 
x = 0
for _ in range(12):
    print(x, end=' ')
    if x == 0:
        x += 1
    elif x < 256:
        x *= 2