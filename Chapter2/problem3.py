# Check the type of variable assigned using input () function

a = input("Enter the variable: ")
if a.isdigit():
    a = int(a)

print(type(a))