N = int(input())
b = [input().split() for _ in range(N)]

class mate():
    def info(self, nickname, old, birth, state):
        self.nickname = str(nickname)
        self.old = int(old)
        self.birth = str(birth)
        self.state = str(state)

    def infos(self):
        return ('User{{\n'
        'nickname : {0}\n'
        'old : {1}\n'
        'birth : {2}\n'
        'state : {3}\n'
        '}}').format(self.nickname , self.old, self.birth, self.state)

class mates(mate):
    def __init__(self,N,b):
        self.N = N
        self.b = b
        self.labels =  ["nickname", "old", "brith", "state"]
        self.data = [self.b[i] for i in range(N)]
        self.meibo = []
    
    def narabel(self, row_name):
        self.row_name = str(row_name)
        for i in range(len(self.labels)):
            if self.row_name == self.labels[i]:
                iter = i
        self.data = sorted(self.data, key= lambda x:x[iter])
        return self.data
        

mates = mates(N, b)
mates.narabel("old")
for data in mates.data:
    print(*data)



