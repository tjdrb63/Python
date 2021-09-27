Str = input()
Count = []
Max = "0"
Str = Str.lower()

for i in range(97,123):
    Count.append(Str.count(chr(i)))

MaxCount = max(Count)

for (i,s) in enumerate(Count):
    if s == MaxCount:
        if(Max != "0"):
            print("?")
            exit()
        Max = chr(i+97)

print(Max.upper())







