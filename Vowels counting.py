# to count vowels in the given string
text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(f"Number of vowels: {count}")
