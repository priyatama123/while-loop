a=int(input("enter number"))
p=a
rev=0
while a>0:
    b=a%10
    rev=(rev*10)+b
    a=a//10
    if p==rev:
        print("palindrome num")
    else:
        print("not polindrome")
            

