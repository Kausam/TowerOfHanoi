def solve(n,fr,to):
    if(n==1):
        print(fr,'->',to)
        return
    if(fr+to==3):
        rem=3
    elif(fr+to==5):
        rem=1
    else:
        rem=2
    solve(n-1,fr,rem)
    solve(1,fr,to)
    solve(n-1,rem,to)
n=int(input())
solve(n,1,2)

