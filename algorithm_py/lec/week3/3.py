### 과제3.

'''
다음은 Tree 자료구조를 순회하는 방법 중, Pre-order 순회 방법을 설명한 것이다. 자료구조의 순회란, 자료구조에 속한 모든 data를 한 번씩 접근하는 것이다. Pre-order 순회를 하면서 순회한 순서대로 Node의 data를 콘솔에 출력하는 preorder() 메소드를 완성하시오.

Tree 자료구조를 순회할 때에는 반드시 root node부터 순회를 시작한다.
Pre-order 순회를 할 때에는 아래와 같은 방법을 재귀적으로 수행한다.
새로운 node에 접근할 경우, 아래 순서대로 동작한다.
Node에 있는 data를 출력한다.
Node에 left child가 있으면, left child node에 접근한다.
Node에 right child가 있으면, right child node에 접근한다.
root node에서 순회를 시작할 경우, 재귀적 동작으로 인해 모든 node의 data를 출력할 수 있다.
'''

'''
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
class Tree:
    def __init__(self, root):
        self.root = root
 
    def preorder(self):
        pass
 
# Test code
root = Node(5, Node(2, Node(7, Node(4), Node(1)), Node(3)), Node(9, Node(6), Node(10)))
tree = Tree(root)
tree.preorder()

# 출력
5
2
7
4
1
3
9
6
10

'''


# 내 풀이 ----------------------------------------------------------------------------
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
class Tree:
    def __init__(self, root):
        self.root = root
 
    def preorder(self):
        def preorder1(root):
            if root is None:
                pass
            else:
                print(root.data)
                preorder1(root.left)
                preorder1(root.right)
        preorder1(self.root) 



# Test code
root = Node(5, Node(2, Node(7, Node(4), Node(1)), Node(3)), Node(9, Node(6), Node(10)))
tree = Tree(root)
tree.preorder()

# 강사님 풀이 ------------------------------------------------------------------------- 
#Tree의 Preorder traversal(depth-firsth traversal)을 구현하는 문제였습니다.
#재귀함수를 이용하여 구현하면 쉽게 구현할 수 있습니다.
#아래 예시 답안을 확인해 주세요 :)

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
class Tree:
    def __init__(self, root):
        self.root = root
 
    def preorder(self):
        def recursion(node):
            print(node.data, end=' ')
            if node.left:
                recursion(node.left)
            if node.right:
                recursion(node.right)
        recursion(self.root)
 
 
