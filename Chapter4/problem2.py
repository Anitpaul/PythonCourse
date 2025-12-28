print("Enter marks of of 6 students: ")

l1 = []
for i in range(0, 6):
    temp = int(input(f"{i+1}: "))
    l1.append(temp)
l1.sort()
print(l1)