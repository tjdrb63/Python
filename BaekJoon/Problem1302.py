Str = {}
outPut = []
for i in range(int(input())):
    cnt = 0
    Key=input() 
    if(Key in Str):
         cnt=Str[Key]
    cnt+=1
    Str[Key] = cnt
    
maxValue = max(Str.values())

for s in Str.keys():
        
    if(Str[s] == maxValue):
        outPut.append(s)
outPut.sort()

print(outPut[0])