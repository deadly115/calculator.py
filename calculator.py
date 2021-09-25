print=("enter 1 for addition")
print=("enter 2 for subtraction")
print=("enter 3 for multiplication")
print=("enter 4 for division")

choice=int(input("enter  your choice"))
if choice>0 and choice<5:
    num1=int(input("enter the first value"))
    num2=int(input("enter the second value"))
if choice==1:
    num=num1+num2
    print(+num)
elif choice==2:
    num=num1-num2
    print(+num)
elif choice==3:
    num=num1*num2
    print(+num)
else:
    num=num1%num2
    print(+num)
