N, k = map(int, input().split())
b = [input().split() for _ in range(N)]
c = [input().split() for _ in range(k)]

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

    def henko(self, k, c):
        self.k = int(k)
        self.c = c
        for i in range(self.k):
            bango = int(self.c[i][0])-1
            self.data[bango][0] = self.c[i][1]
        return self.data

    def make_meibo(self, row_name="None"): #結局使わず、なんでや
        self.row_name = str(row_name)
        if self.row_name != "None":
            self.narabel(self.row_name)
        for i in range(self.N):
            super().info(self.data[i][0], self.data[i][1], self.data[i][2], self.data[i][3])
            self.meibo.append(super().infos())
        return self.meibo


mates = mates(N, b)
mates.henko(k, c)
for data in mates.data:
    print(*data)



