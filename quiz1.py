# Ask user for two numbers
num1 = input("What is your first number?")
num2 = input("What is your second number?")
# Create a loop that does the following until the product and sum are the same

# Calculate and disply their sum
sum=(int(num1)+int(num2))
print(str(sum))
# Calculate and display their product
prod=(int(num1)*int(num2))
print(str(prod))
prod=(int(num1)*int(num2))
print(str(prod))
# If their sum and their product are equal - tell the user
if(sum==prod):
    print("Your sum and product are equal!")
# otherwise ask for two more numbers
else:
    print("Try again!")
    num1 = input("What is your first number?")
    num2 = input("What is your second number?")
    sum = (int(num1) + int(num2))
    print(str(sum))
    prod = (int(num1) * int(num2))
    print(str(prod))