print("Enter a number")

number = int(input())

for i in range(10):
    result = i * number
    print(str(i) + " x " + str(number) + " = " + str(result))