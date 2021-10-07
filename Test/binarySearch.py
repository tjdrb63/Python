list = [1,2,3,10,40,50,60,77,86,94,1012,11213,12333,13444]
key =int(input())
min = 0
max = len(list)-1

while min<=max:
    half = (max+min) // 2
    
    if(list[half]==key):
        print(half+1,"번째에 있습니다")
        break

    if(list[half]>key):
        max=half-1
    
    elif(list[half]<key):
        min=half+1

if(min>max):
    print("결과가 없습니다")
