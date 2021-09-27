def reverse(num):
    cnt = 0 
    for i in range(3):
        cnt += int(num[i])*pow(10,i)
    return cnt

num1, num2 = input().split()

rev_num1 = reverse(num1)
rev_num2 = reverse(num2)

if(rev_num1 > rev_num2):
    print(rev_num1)
else:
    print(rev_num2)