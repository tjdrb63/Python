list = [1,5,4,3,2,6,8,9]
low = 0 
high = len(list)

def merge(a,b):
    maxA = len(a)
    maxB = len(b)
    countA = 0
    countB = 0
    arr = []
    while(True):
        if a[countA] < b[countB]:
            arr.append(a[countA])
            countA += 1
        else:
            arr.append(b[countB])
            countB += 1
        if(countA == maxA) :
            arr.append(b[countB:maxB-1])
            break
        elif(countB == maxB) :
            arr.append(a[countA:maxA-1])
            break

def merge_sort(list,low,high):
    if(len(list)==1) :
        return list
    mid = (high+low)//2
    a = merge_sort(list[low:mid],low,mid)
    b = merge_sort(list[mid:high],low,mid)
    merge(a,b)


merge_sort(list,low,high)