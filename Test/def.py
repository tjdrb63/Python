# def Test_def():
#     print("dd")

# def add(num1 , num2):
#     print(num1+num2)

# def bigger(num1 , num2):
#     if num1 > num2:
#         print(num1)
#     else: 
#         print(num2)

# def hello(age, name="장성규"):
#     print(name,age)

# hello(10,"박주형")

# def print_tp(*t):
#     print(t)

# def print_dic(**t):
#     print(t)

# print_tp(1,2,3,4,5)
# print_dic(first=1,second=2,third=3)


# def sum_int(*arr):
#     sum=0
#     for a in arr:
#         if type(a) is int:
#             sum += a
#     print(sum)

# sum_int(1,2.0,3,4.0,2.1)

# def params(a, *b ,c=4 ,d):
#         print(a,b,c,d)

# params(1,2,3,c=6,d=5)

# def add_return(num1 , num2):
#     return num1+num2
# cnt = add_return(1,2)

# print(cnt)

# def int_func():
#     return {1,2,3}

# def float_func():
#     return {1,2,3}

# print(int_func(),type(float_func()))    

# def list_min(arr):
#     min = 100000
#     for i in arr:
#         if(i<min):
#             min=i
#     return min
    
# print(list_min([201,242,50,429]))

# def func():
#     return 1,2,3

# tp = func()
# print(type(tp))

# def info(*arr):
#     sum=0
#     for a in arr:
#         sum += a
#     avg = sum/len(arr)
#     return sum, avg
# sum,avg = info(*[2,2,4,4,6])
# print(sum,avg)

# sum =0
# def total(values):
#     global sum
#     for i in values:
#         sum += i
#     return sum
# print(total([1,2,3]))


# def print


# def my_range(*num):
#     step = 1
#     leng = len(num)
#     if(leng == 1):
#         start = 0
#         end = num[0]
#     elif(leng ==2):
#         start = num[0]
#         end =num[1]
#         if(leng>2):
#             step= num[2]
#     while start<end:
#         yield start
#         start += step


# arr = [i for i in my_range(5)]
# print(arr)


def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2

def executor(func,op,num1,num2):
    return func[op](num1,num2)

# func = {'+':add,'-':sub}
# print(executor(func,'+',10,20))
# print(executor(func,'-',10,20))

# def get_func(op):
#     if(op == '+'):
#         return add
#     else:
#         return sub

# result = get_func('+')(1,30)
# print(result)

# def func():
#     value =2
#     def nonlocal_func():
#         value = 3 
#         print(value)
#     nonlocal_func()
#     print(value)
# func()

num = 100
try:
    num=int(input())
except ValueError:
    num=0
finally:
    print(num)

