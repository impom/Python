print("Give two numbers as  input")
a = int(input("First number: "))
b = int(input("Second number: "))
sum = a + b
catch ValueError:
    print("Please enter valid integers.")
    exit(1)
print("The sum is: ", sum)