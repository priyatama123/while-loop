a=int(input("enter 1st number"))
i=1
while i<=9:
    b=int(input("enter 2nd number"))
    if b==a:
        print("you guess is right")
        break
    i=i+1
else:
    print("you guess is wrong")
        