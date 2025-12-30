n = input("Enter four numbers: ").split(" ")

n = list(map(int, n))

n.sort()
print("The larget number is: ", n[0])