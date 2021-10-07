list = []
front = 0
rear = 0
def put(num):
    global front
    front += 1
    list.append(num)
    
def get():
    global rear
    cnt =list[rear]
    list[rear] = 0
    rear +=1
    return cnt 



while(True):
    s = int(input())
    if(s == 1):
        print("push :",end=' ')
        num = int(input())
        put(num)
    elif(s == 2):
        print("Value : ",get())
    else:
        break
    
    print(list)