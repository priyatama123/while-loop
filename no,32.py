a=int(input("enter number"))
i=1
sum=0
while i<=a:
    if i%2==0:
        print(i*i)
    else:
        print("-",i*i) 
    i=i+1
    sum=sum+i
print(sum) 
