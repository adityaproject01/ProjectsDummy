a=100
flag=False
if a==1:
    print("number is not original")
elif a>1:
    for i in range(2,a):
        if a%i==0:
            print(i)
        else:
            print(i,"id prime")
   
        