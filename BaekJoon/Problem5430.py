import sys
count = int(input())

for i in range(count):
    ch = 0
    rev = 1
    AC = sys.stdin.readline()
    listcount = int(input())
    list = sys.stdin.readline().strip(' [ \n ] ').split(',')   

    for j in range(len(AC)):
        command = AC[j]
        if(command == 'R'):
            rev=rev*-1
            
        elif(command == 'D'):
            if(listcount < 1):
                print('error')
                ch = 1
                break
            
            if(rev == 1):
                list.pop(0) 
            elif(rev==-1):
                list.pop()
            listcount -= 1

    if(rev == -1):
        list.reverse()

    if(ch == 0):
        print('[',end="")
        for x in range(len(list)):
            if(x!=0):
                print(',',end="")
            print(list[x],end="")
        print(']')

