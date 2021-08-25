###과제3.

'''
아래 기반 코드를 완성하여, 주어진 출력을 하는 클래스를 구현하시오. 단, Animal 클래스는 수정하지 않고 구현하시오. 최소한의 메소드만을 추가하여 구현하시오. 하나의 메소드는 하나의 line만을 출력하시오.
'''

'''
출력
Nancy cannot speak.
Nancy moves like a jagger.
Michael is smart enough to speak.
Michael moves like a jagger.
'''

# 내 풀이 ----------------------------------------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print(self.name + ' cannot speak.')
 
    def move(self):
        print(self.name + ' cannot move.')
 
 
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(self.name + ' moves like a jagger.')
 
 
class Retriever(Dog):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):            
        print(self.name + ' is smart enought to speak.')            
 
dog = Dog('Nancy')
dog.speak()
dog.move()
 
super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move() 

# 강사님 풀이 ------------------------------------------------------------------------- 
#클래스의 상속을 이해하고, 이를 직접 구현하는 문제였습니다.
#상속과 오버라이딩을 잘 이해하고 구현해 주셨습니다 :)

class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print(self.name + ' cannot speak.')
 
    def move(self):
        print(self.name + ' cannot move.')
 
 
class Dog(Animal):
    def move(self):
        print(self.name + ' moves like a jagger.')
 
 
class Retriever(Dog):
    def speak(self):
        print(self.name + ' is smart enough to speak.')
 
 
dog = Dog('Nancy')
dog.speak()
dog.move()
 
super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()