s = input()
num_cnt = [3,3,3,4,4,4,5,5,5,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
count = 0
for i in range(len(s)):
    count += num_cnt[ord(s[i])-65]
print(count)