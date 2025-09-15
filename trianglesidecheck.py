a = float(input("enter side 1 : "))
b = float(input("enter side 2 : "))
c = float(input("enter side 3 : "))
if a+b > c and a+c > b and c+b> a :
    print("sides form a valid triangle")
else:
    print("sides do not form a valid triangle")

