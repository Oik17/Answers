
fifth = ""
sum = count = 0
even = odd = None
flag1 = flag2 = False
for i in range(10):
    n=int(input())
    if i==4:
        fifth=str(n)
    if n%2 == 0:
        flag1 = True
        if even is None or n<even:
            even=n
    else:
        flag2 = True
        if odd is None or n>odd:
            odd=n
if flag1 and flag2:
    print(odd+even)
elif flag1 and flag2==False:
    for i in fifth:
        sum += int(i)
    print(sum)
elif flag1==False and flag2:
    for i in fifth:
        count+=1
print(count)