#pizza order
size=input("enter your order size S/M/L= ").lower()
bill=0
if size == "s"  :
    bill+=100
    print(f"great choice! , you chosse Small Size")
    print("you have to pay 100 rupee")
elif size == "m" :
    bill+=150
    print(f"great choice! , you chosse Midum Size")
    print("you have to pay 150 rupee")
elif size== "l":
    bill+=200
    print(f"great choice! , you chosse Large size")
    print ("you have to pay 200 rupee")
else:
    print("please enter sufficient Size")


cheese=input("do you want to add extra  cheese y/n  ").lower()


if cheese=="y":
    if size =="s":
        bill+=30
    else:
        bill+=50
pepperoni=input("do yo want ot add pepperoni y/n  ").lower()
if pepperoni=="y":
    if size=="l" or size=="m"  :
        bill+=70
    else:
        bill+=40
item=int(input("please enter quantity"))
price=item*bill

print(f"your final bill is:  ",price," rupees only ")
print(" thank you !")

