N = int(input())
a = list(map(int, input().split()))

a.sort()
p = []
while len(a) != 0:
    p.append(a.pop(0)+a.pop(-1))
p.sort()
print(p[-1]-p[0])




