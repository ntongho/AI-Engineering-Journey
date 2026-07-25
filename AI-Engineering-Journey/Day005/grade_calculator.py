
score = int(input("Enter a score"))
if 90 <=score <=100: #this is a better method instead on the too many and
    print("A")
elif score>=80 and score <=89:
    print("B")
elif score>=70 and score <=79:
    print("C")
elif score>=60 and score <=69:
    print("D")
elif score<60:
    print("F")
else:
    print("Invalid score")

