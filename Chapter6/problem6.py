m = int(input("Enter your Mark: "))

if m <= 100:
    # 90 – 100 => Ex 
    if m >= 90:
        val = "Ex"
    # 80 – 90 => A
    elif m >= 80:
        val = "A"
    # 70 – 80 => B
    elif m >= 70:
        val = "B"
    # 60 – 70 =>C
    elif m >= 60:
        val = "C"
    # 50 – 60 => D
    elif m >= 50:
        val = "D"
    # <50 => F
    elif m < 50:
        val = "F"

    print(f"The child  with {m} marks has got: {val}")
else:
    print("Wrong Input Please enter your marks!")