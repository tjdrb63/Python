coin_length,won = map(int,input().split())
coin_list= []
count = 0

for i in range(0,coin_length):
    coin_list.append(int(input()))  

while won>0:
    if coin_list[i]<=won:
        check_money = coin_list[i]
        check_count=int(won/check_money)
        count+=check_count
        won-=check_money*check_count
    else:
        i -= 1

print(count)