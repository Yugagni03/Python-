# question 1
num1=int(input("Enter the value of num1 : "))
num2=int(input("Enter the value of num2 : "))
num3=int(input("Enter the value of num3 : "))
num4=int(input("Enter the value of num4 : "))
if((num1>num2) and (num1>num3) and (num1>num4)) :
    print("num1 is greater !! ")
elif((num2>num1) and (num2>num3) and (num2>num4)) :
    print("num2 is geater !! ")
elif((num3>num1) and (num3>num2) and (num3>num4)) :
    print("num3 is greater !!")
else :
    print("num4 is greater")   

# question 2
sub1=int(input("Enter the value of sub1 : "))
sub2=int(input("Enter the value of sub2 : "))
sub3=int(input("Enter the value of sub3 : "))
sub4=int(input("Enter the value of sub4 : "))
total=(sub1+sub2+sub3+sub4)
if(total==33) :
    print("pass")
elif(total>40) :
    print("congratulations !!")
else :
    print("try hard , you can di it !!")