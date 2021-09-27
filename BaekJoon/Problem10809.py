s = input()
cnt = [-1 for i in range(26)] 
maxcount = len(s)
for i in range(maxcount):
    now = s[maxcount-i-1]
    cnt[ord(now)-97] = maxcount-i-1

for i in cnt:
    print(i,end=' ')
