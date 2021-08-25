###과제1.

''' 
아래 주어진 기반 코드를 완성하여 Linked Queue를 구현하시오. Linked Queue에 대한 설명을 참조하시오.

Linked Queue의 특징
Linked Queue는 Doubly Linked List를 기반으로 만들어진 Queue이다.
Linked Queue의 모든 동작은 O(1)의 시간복잡도로 동작한다.
Linked Queue에 정의된 동작은 아래와 같다.
is_empty(): Queue가 비어있으면 True, 비어있지 않으면 False를 반환한다.
put(): Queue의 rear에 새로운 데이터를 입력한다.
get(): Queue의 front에서 데이터를 반환한다. 출력한 데이터는 Queue에서 삭제한다. 더이상 출력할 데이터가 없는 경우 None을 반환한다.
peek(): Queue의 front에서 데이터를 반환한다. 반환한 데이터는 Queue에 그대로 유지한다. 반환할 데이터가 없는 경우 None을 반환한다.
'''

'''
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
 
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
 
    def is_empty(self):
        pass
 
    def put(self, data):
        pass
 
    def get(self):
        pass
 
    def peek(self):
        pass
 
# Test code
queue = LinkedQueue()
 
print(queue.is_empty())
for i in range(10):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(11):
    print(queue.get(), end=' ')
print()
 
for i in range(20):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(5):
    print(queue.peek(), end=' ')
print()
 
for _ in range(21):
    print(queue.get(), end=' ')
print()
print(queue.is_empty())

출력
True
False
0 1 2 3 4 5 6 7 8 9 None 
False
0 0 0 0 0 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 None 
True
'''

# 내 풀이 ----------------------------------------------------------------------------
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
 
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
 
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
 
    def put(self, data):
        if self.rear is None:            
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.next = Node(data)            
            self.rear.next.prev = self.rear
            self.rear = self.rear.next
 
    def get(self):
        if self.front is None:
            return None
        else:
            val = self.front.data
            if self.front.next is not None:
                self.front = self.front.next
                self.front.prev = None              
            else:
                self.front = self.front.next
                self.rear = None                                            
            return val
 
    def peek(self):
        return self.front.data

# Test code
queue = LinkedQueue()
 
print(queue.is_empty())                 
for i in range(10):
    queue.put(i)                        
print(queue.is_empty())                 
 
for _ in range(11):
    print(queue.get(), end=' ')         
print() 
 
for i in range(20):
    queue.put(i)
print(queue.is_empty())                 
 
for _ in range(5):
    print(queue.peek(), end=' ')        
print()
 
for _ in range(21):
    print(queue.get(), end=' ')         
print()
print(queue.is_empty())                 

# 강사님 풀이 ------------------------------------------------------------------------- 
#수업시간에 배운 Doubly Linked List를 이용하여 Linked Queue를 구현하는 문제였습니다.
#기능을 잘 구현해 주셨습니다! 아래 예시답안을 첨부하니 참고해 주세요 :)

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
 
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
 
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
 
    def put(self, data):
        if self.rear is None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear = Node(data, self.rear, None)
            self.rear.prev.next = self.rear
 
    def get(self):
        if self.front is None:
            return None
        elif self.front is self.rear:
            data = self.front.data
            self.front, self.rear = None, None
        else:
            data = self.front.data
            self.front = self.front.next
            self.front.prev = None
        return data
 
    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front.data