#the code to reverse a number

num = int(input("Enter a number: "))
reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print(f"Reverse of {num} is {reverse}")

'''
# reversing a text using slicing 
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
'''