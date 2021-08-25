###과제4.

'''
HashTable 클래스는 문자열을 key로 입력받는 해쉬 테이블 자료구조를 구현한 것이다. HashTable 클래스는 단순한 해쉬 함수로 인해, 해쉬 충돌이 빈번히 발생한다. 이 단점을 개선하기 위해, Chaining 기법으로 ChainedHashTable을 구현하고자 한다.

HashTable을 상속하여 해쉬 충돌이 발생해도 정상적으로 동작하는 ChainedHashTable을 완성하시오.
'''

'''
def hash_func(key):
    return ord(key[0]) % 10
 
class HashTable:
    def __init__(self):
        self.table = [None]*10
 
    def set(self, key, value):
        self.table[hash_func(key)] = value
 
    def get(self, key):
        return self.table[hash_func(key)]
 
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
 
class ChainedHashTable(HashTable):
    pass
 
# Test code
 
ht = ChainedHashTable()
ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)
 
print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
print()
 
ht.set('hello2', 5)
 
print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')

출력
1 2 3 4
1 5 3 4
'''

# 내 풀이 ----------------------------------------------------------------------------

# 풀이 없음

# 강사님 풀이 ------------------------------------------------------------------------- 
#Hash Table에서 Chaining 기법을 구현하는 문제였습니다.
#수업시간에 배운 list를 이용하는 방법을 사용해도 되며, 아래 Node를 이용하는 예시 답안도 확인해 주세요 :)

def hash_func(key):
    return ord(key[0]) % 10
 
class HashTable:
    def __init__(self):
        self.table = [None]*10
 
    def set(self, key, value):
        self.table[hash_func(key)] = value
 
    def get(self, key):
        return self.table[hash_func(key)]
 
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
 
class ChainedHashTable(HashTable):
    def __init__(self):
        super().__init__()
 
    def set(self, key, value):
        idx = hash_func(key)
        if self.table[idx] is None:
            self.table[idx] = Node(key, value)
        else:
            node = self.table[idx]
            while node.next is not None:
                if node.key == key:
                    node.data = value
                    return
                node = node.next
            node.next = Node(key, value)
 
    def get(self, key):
        idx = hash_func(key)
        if self.table[idx] is None:
            return None
        else:
            node = self.table[idx]            
            while node.next is not None:
                if node.key == key:
                    return node.data
                node = node.next
            if node.key == key:
                return node.data
            else:
                return None
 
ht = ChainedHashTable()
ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)
 
print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
print()
 
ht.set('hello2', 5)
 
print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')