def Test(x):
    yield x

arr = [i for i in Test(5)]
print(arr)
