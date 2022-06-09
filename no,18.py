binary=int(input("enter number"))
d=0
i=1
while binary!=0:
    rev=binary%10
    d=d+rev*i
    i=i*2
    print(d)


