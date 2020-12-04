for i in range(int(input())):
    a,b =map(int,input().split())
    n=int(input())
    start = a
    end = b
    while start <= end:
        mid = (start+end)//2
        print(mid)
        b=input()
        if b == "Correct":
           break
        elif b=="Wrong Answer":
           break
        elif b=="Too Small":
            start = mid+1
        elif b=="Too Big":
            end = mid

        
