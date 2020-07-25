class Node:
    def __init__(self, value, left = None, right=None):
        self.value = value
        self.left = left
        self.right =  right


def preOrder_iter(head):
    if head is None:
        return
    stack = []
    stack.append(head)
    while stack:
        head = stack.pop()
        print(head.value, end=' ')
        if head.right:
            stack.append(head.right)
        if head.left:
            stack.append(head.left)



root=Node(1,Node(2), Node(3))
preOrder_iter(root)

if __name__ == '__main__':

    pass