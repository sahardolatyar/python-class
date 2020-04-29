def fib1(n):

        if n==1 or n==2:
           return 1
        return fib1(n-1)+fib1(n-2)
l1=[]
def fib2(n):
    i=n
    while n:
        if fib1(n) not in l1:
            l1.append(fib1(n))
        n -=1
    if i>1:
       l1.append(1)
    l2=l1.copy()
    l1.clear()
    return l2
