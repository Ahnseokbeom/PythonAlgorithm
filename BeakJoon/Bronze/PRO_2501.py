def prime(n,k):
    n_list = []
    for i in range(1,n+1):
        if n%i==0: n_list.append(i)
    if len(n_list)<=k-1:
        print(0)
    else: print(n_list[k-1])
    
n,k = map(int,input().split())
prime(n,k)
    