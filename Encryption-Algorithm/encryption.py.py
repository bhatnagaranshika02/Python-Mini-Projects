n = int(input())
a = input()
b=[]
flag=0
for i in a:
    if ord(i) == 97 or ord(i) == 65:
        b.append(chr(ord(i)+25))
    elif i.isupper():
        b.append(chr(90 - abs((65 - ord(i)))))
    elif i.islower():
        b.append(chr(122 - abs ((97 - ord (i)))))
    else:
        flag=1
        break

if flag==0:
    print(*b,sep='')
if flag==1:
    print('Invalid')
