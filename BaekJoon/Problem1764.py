n,m = map(int,input().split())
Dic = {}
outPut = []
for i in range(n):
    Dic[input()]=1

for i in range(m):
    cnt = input()
    if(cnt in Dic):
        outPut.append(cnt)

outPut.sort()
print(len(outPut))
for s in outPut:
    print(s)
