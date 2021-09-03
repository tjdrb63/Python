count = int(input())
resultlist=[]
for j in range(0,count):
    num1,num2 = map(int,input().split())
    numlist =[]
    check = num1 
    for i in range(0,num2):
        if(num1>10): 
            num1=num1%10    
        try:
            numlist.index(num1)
            break
        except:
            numlist.append(num1)
        num1*=check

    result = (num2-1)%len(numlist)
    resultlist.append(numlist[result])
for res in resultlist:
    print(res)