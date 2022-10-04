from collections import deque

class pile(deque):
    def __init__(self):
        deque.__init__(self)
    def empiler(self, item):
        self.append(item)
    def depiler(self):
        self.pop()
p = pile(["kawtar", "ouafae", "zikou", "karim"])
p.empiler(0)
p.empiler(5)
p.empiler(10)
p.empiler(15)
print(p.depiler())
print(p.depiler())

class file(deque):
    def __init__(self):
        deque.__init__(self)
    def emfiler(self, item):
        self.append(item)
    def defiler(self):
        self.popleft()
p = file(["kawtar", "ouafae", "zikou", "karim"])
p.emfiler(0)
p.emfiler(5)
p.emfiler(10)
p.emfiler(15)
print(p.defiler())
print(p.defiler())

class PriorityQueue():
    def __init__(self):
        self.file = []
    def empty(self):
        if len(self.file) == 0:
            return 0
    def emfiler(self, data):
        self.file.append(data)
    def defiler(self):
        max = 0
        for i in range(len(self.file)):
            if self.file[i] >= self.file[max]:
                max = i
        del self.file[max]


