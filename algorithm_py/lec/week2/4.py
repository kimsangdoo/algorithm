###과제4.

'''
아래 기반 코드를 완성하여, 주어진 출력을 하는 클래스를 구현하시오. 기반 코드에 제시된 대로 print문 하나당 문자 하나씩만 출력하시오.
'''

'''
class Foo:
    pass
 
print(Foo.bar)       # A 출력
print(Foo().bar)     # B 출력
print(Foo.Bar.bar)   # C 출력
print(Foo.Bar().bar) # D 출력
'''


'''
출력
A
B
C
D
'''

# 내 풀이 ----------------------------------------------------------------------------
class Foo:
    bar = 'A'    
    def __init__(self):        
        self.bar = 'B'

    class Bar:
        bar = 'C'
        def __init__(self):
            self.bar = 'D'

print(Foo.bar)       # A 출력
print(Foo().bar)     # B 출력
print(Foo.Bar.bar)   # C 출력
print(Foo.Bar().bar) # D 출력

# 강사님 풀이 ------------------------------------------------------------------------- 
#클래스 변수와 인스턴스 변수를 이해하고 구현하는 문제였습니다.
#중첩 클래스까지 활용하면 주어진 과제를 모두 해결하실 수 있습니다. :)

class Foo:
    bar = 'A'
    def __init__(self):
        self.bar = 'B'
 
    class Bar:
        bar = 'C'
        def __init__(self):
            self.bar = 'D'
 
print(Foo.bar)       # A 출력
print(Foo().bar)     # B 출력
print(Foo.Bar.bar)   # C 출력
print(Foo.Bar().bar) # D 출력