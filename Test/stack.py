list = [0]*10
top = 0 
def push(num):
    global top
    if(top>9):
        print("Stack OverFlow")
        return 

    list[top]=num
    top += 1


def pop():
    global top
    if(top==0):
        print("Stack Empty")
        return

    cnt = list[top-1]
    list[top-1]=0
    top-=1
    return cnt

push(0)
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
push(9)
push(10)
push(11)
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(list)