class MinStack:
    def __init__(self):
        self.main_stack=[]
        self.min_stack=[]
    def __repr__(self):
        return '-- main_stack:'+str(self.main_stack)+'\n-- min_stack:'+str(self.min_stack)

    def push(self,e):
        self.main_stack.append(e)
        if len(self.min_stack) == 0 or e <= self.min_stack[len(self.min_stack)-1]:
            return self.min_stack.append(e)

    def pop(self):
        if self.main_stack[len(self.main_stack)-1]==self.min_stack[len(self.min_stack)-1]:
            self.min_stack.pop()
        return self.main_stack.pop()


    def get_min(self):
        if len(self.main_stack)==0:
            return None
        return self.min_stack[len(self.min_stack)-1]



s = MinStack()
s.push(4)
s.push(3)
s.push(5)
print(s)
print(s.get_min())
print(s.pop())
print(s)
print(s.get_min())
print(s.pop())
print(s)
print(s.get_min())
print(s.pop())
print(s)
print(s.get_min())



if __name__ == '__main__':
    pass

# 4,3,5
#1,
#a 4
#b 4
#2
#a 4 3
#b 4 3
#3
#a 4 3 5
#b 4 3
#4 get_min
#