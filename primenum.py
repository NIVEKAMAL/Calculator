
x=int(input('enter the numbers:'))
for num in range(1,x):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
             print(num)
