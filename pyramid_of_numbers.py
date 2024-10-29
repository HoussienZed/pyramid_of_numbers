# asking user to enter a number x

x = int(input("Enter an integer: "))

# printing pyramid

for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")
