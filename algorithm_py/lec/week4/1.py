### 과제1.

'''
Min Heap 자료구조를 이용하면 최대값을 O(logN)의 시간복잡도로 찾을 수 있다. Min Heap을 이용하면 우선순위 값이 낮은 자료를 먼저 출력하는 Priority Queue를 구현할 수 있다. Min Heap을 이용한 Priority Queue는 아래와 같은 특징을 가진다.

Min Heap을 이용한 Priority Queue의 특징
자료를 입력하는 동작과 출력하는 동작 모두 O(logN)으로 이루어진다.
우선순위 값이 낮은 자료를 먼저 출력하되, 우선순위 값이 같은 자료끼리는 순서를 고려하지 않는다.
다음과 같은 Method들을 구현한다.
is_empty(): Queue가 비어있으면 True, 비어있지 않으면 False를 출력한다.
put(): Priority Queue에 자료를 입력한다. 자료는 길이가 2인 Tuple로, (우선순위, 자료) 형태로 입력받는다.
get(): Priority Queue에서 자료를 출력한다. 출력한 데이터는 Priority Queue에서 삭제한다. 더이상 출력할 데이터가 없는 경우 None을 출력한다.
peek(): Priority Queue에서 자료를 출력한다. 출력한 데이터는 Priority Queue에 그대로 유지한다. 더이상 출력할 데이터가 없는 경우 None을 출력한다.
'''

'''
class PriorityQueue:
    def __init__(self):
        pass
 
    def is_empty(self):
        pass
 
    def put(self, data):
        pass
 
    def get(self):
        pass
 
    def peek(self):
        pass

# Test code 
pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))
 
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
'''


# 내 풀이 ----------------------------------------------------------------------------

# 없음

# 강사님 풀이 ------------------------------------------------------------------------- 
#수업시간에 배운 Heap 구조를 이용하여 PriorityQueue를 구현하는 문제였습니다.
#Heap 구조를 직접 구현해 주셔야 하며, 다른 방법을 사용할 경우 시간복잡도 조건이 맞지 않게 됩니다.
#Heap을 구현하시되, 입력을 우선순위와 데이터 2가지를 함께 입력받는 형식으로 구현하시면 됩니다.

class PriorityQueue:
    def __init__(self):
        self.tree = [None]
 
    def is_empty(self):
        return len(self.tree) == 1
 
    def put(self, data):
        self.tree.append(data)
        curr = len(self.tree) - 1
        parent = curr // 2
        while parent > 0:
            if self.tree[curr][0] > self.tree[parent][0]:
                return
            self.tree[curr], self.tree[parent] = self.tree[parent], self.tree[curr]
            curr = parent
            parent = curr // 2
 
    def get(self):
        if self.is_empty() is True:
            return None
        data = self.tree[1]
        self.tree[1] = self.tree[-1]
        self.tree = self.tree[:-1]
        curr = 1
        while curr < len(self.tree):
            left = curr * 2
            right = curr * 2 + 1
            if left < len(self.tree) and right < len(self.tree):
                if self.tree[left][0] < self.tree[right][0]:
                    if self.tree[left][0] < self.tree[curr][0]:
                        self.tree[curr], self.tree[left] = self.tree[left], self.tree[curr]
                        curr = left
                else:
                    if self.tree[right][0] < self.tree[curr][0]:
                        self.tree[curr], self.tree[right] = self.tree[right], self.tree[curr]
                        curr = right
 
            elif left < len(self.tree) and self.tree[left][0] < self.tree[curr][0]:
                self.tree[curr], self.tree[left] = self.tree[left], self.tree[curr]
                curr = left
            elif right < len(self.tree) and self.tree[right][0] < self.tree[curr][0]:
                self.tree[curr], self.tree[right] = self.tree[right], self.tree[curr]
                curr = right
            else:
                break
        return data
 
    def peek(self):
        if self.is_empty() is True:
            return None
        return self.tree[1]
 
pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))
 
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())