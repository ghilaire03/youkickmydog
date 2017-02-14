min=int(input("enter your range... min: "))
max=int(input("enter your range...  Max:"))
for num in range(min,max):
    for x in range(2,num):
        if(num%x==0 and num!=1):
            break
        else:
            print(num," is prime")
            break