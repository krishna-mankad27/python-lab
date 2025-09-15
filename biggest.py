x = int(input("enter num 1 : "))
y = int(input("enter num 2 : "))
z = int(input("enter num 3 : "))
if x > y :
    if x > z:
        print(f"{x} is the greatest number")
    elif x < z:
        print(f"{z} is the greatest number")
elif y > x:
    if y > z :
        print(f"{y} is the greatest number")
    elif y < z:
        print(f"{z} is the greatest number")
else :
    print(f"{z} is the greatest number")
