num1=int(input('Enter the number of Math= '))
num2=int(input('Enter the number of English='))
num3=int(input('Enter the number of C++ = '))
num4=int(input('Enter the number of EEE=  '))
num5=int(input('Enter the number of linux = '))
sum=num1+num2+num3+num4+num5
print("sum of two number = ",sum)
per=(sum/250)*100
print("you get percent in MST is = ",per)

if per>90 :
    print(" your Grade is A+")
elif per>80 :
    print("Your grad is A ")
elif per>70 :
    print("your grad is B ")
elif per>50  :
    print("your Grad is C ")
elif per>34 :
    print ("you get passed in Exam")
else:
    print ("you get fail in exam ")
print("thanku"+f"your number ={sum}"+ f"your percent= {per}")