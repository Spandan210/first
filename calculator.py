from ast import Add


print("WELCOME")
num1=int(input("Enter First Number:"))#Data Intake from user
num2=int(input("Enter Second Number:"))
print("As this is a basic calculator program we can :")
print("1.Add")#Facilities provided by the program
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")
sum=(num1+num2)#ARITHMETIC OPERATIONS
dif=(num1-num2)
pro=(num1*num2)
div=(num1/num2)
ope=1#COUNTER FOR LOOP
while ope!=5:#BEGINNING OF WITH THE LOOP ENDING ONLY IF YOU ENTER 5 IN THE QUESTION BELOW
    ope=input("What would you like to do(Specify the Number):")
    if ope=="1" :
        print("Sum: "+str(sum))
    elif ope=="2":
        print("Difference: "+str(dif))
    elif ope=="3":
        print("Product: "+str(pro))
    elif ope=="4":
        print("Division: "+str(div))
    elif ope=="5":
        break#LOOP ENDS 
print("Thank You")
    

    


