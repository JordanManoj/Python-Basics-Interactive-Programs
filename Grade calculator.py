# simple grade calculator
marks = int(input("Enter marks (0-100): "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks <= 89:
    print("Grade: B")
elif 50 <= marks <= 74:
    print("Grade: C")
elif 0 <= marks < 50:
    print("Failed")
else:
    print("Please enter a valid mark.")
