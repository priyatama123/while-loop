a=int(input("enter number"))
b=int(input("enter number"))
sum1=0
sum2=0
while a<=b:
    if a%2==0:
        sum1=sum1+a
    else:
        sum2=sum2+a  
    a=a+1
print(sum1)
print(sum2)
          