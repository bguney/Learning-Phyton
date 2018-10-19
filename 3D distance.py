# Learning-Phyton
def cal(x,y,z,x1,y1,z1):
    return ((x-x1) ** 2 + (y-y1) ** 2 + (z-z1) ** 2) ** 0.5

num1 = int(input("enter the first of first coordinate"))
num2 = int(input("enter the second of first coordinate"))
num3 = int(input("enter the third of first coordinate"))
num4 = int(input("enter the first of second coordinate"))
num5 = int(input("enter the second of second coordinate"))
num6 = int(input("enter the third of second coordinate"))
print(num1,"-",num4, "**2", num2, "-", num5, "**2", num3,"-",num6, "**2", "**0.5", cal(num1, num2, num3, num4, num5, num6))



