N = int(input())
b = [input().split() for _ in range(N)]
k = int(input())

class mate():

    def info(self, name, old, birth, state):
        self.name = str(name)
        self.old = int(old)
        self.birth = str(birth)
        self.state = str(state)

    def duc(self):
        return ('User{{\n'
        'nickname : {0}\n'
        'old : {1}\n'
        'birth : {2}\n'
        'state : {3}\n'
        '}}').format(self.name , self.old, self.birth, self.state)

mate = mate()
for i in range(N):
    mate.info(b[i][0], b[i][1], b[i][2], b[i][3])
    if mate.old == k:
        print(mate.name)

