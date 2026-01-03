marks = {}

marks["English"] = int(input("Enter your English Marks:  "))
marks["Math"] = int(input("Enter your Maths Marks:  "))
marks["Science"] = int(input("Enter your Science Marks:  "))

has_failed = False
for mark in marks.values():
    if mark < 33:
        has_failed = True    

if (sum(marks.values())/300)*100 <= 40:
    has_failed = True

if has_failed:
    print("User has failed!")
else: 
    print("User has passed!")