N = int(input())
b = [input().split() for _ in range(N)]
# b = [0]*N
# for i in range(N):
#     b[i] = input().split()
#     print(b[i])

class mate():
    
    def info(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state

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
    print(mate.duc())
print()
