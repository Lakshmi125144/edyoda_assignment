a = input("Enter word:")
rev = ''
b = len(a) - 1
while b >= 0:
    rev += a[b]
    b -= 1

print("Reversed word:", rev)
