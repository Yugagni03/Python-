a = (int(input("enter num1 :")))
b = (int(input("enter num2 :")))
c = (int(input("enter num3 :")))
d = (int(input("enter num4 :")))
print ("the list is :"+ "[",a,b,c,d, "]")
print ("the list is :"+ "(",a,b,c,d, ")")     # wrong method



values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)