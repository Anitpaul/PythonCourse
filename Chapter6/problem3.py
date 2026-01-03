spams = ["Make a lot of money", "buy now", "subscribe this", "click this"]

sentence = input("Enter your Sentence: ")

c = 0
for spam in spams:
    if spam.lower() in sentence.lower():
        print(f"The spam '{spam}' is found!")
        c += 1

if c == 0:
    print("No spam is found!")


