# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.

num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 =int (input("Enter the third number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is greater")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater") 
else:
    print(f"{num3} is greater") 
    


# Take 4 inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 =int (input("Enter the third number: "))
num4 =int (input("Enter the third number: "))

if num1>num2 and num1>num3 and num1>num4:
    print(f"{num1} is greater")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"{num2} is greater")
elif num3>num1 and num3>num2 and num3>num4:
    print(f"{num3} is greater") 
else:
    print(f"{num4} is greater")  


# Take as input from a user the temperature if the temperature is above 30°C display 
# “The temperature is too high”,if the temperature is above 15 display “Normal temperature” 
# otherwise display “Cold temperature”
 # Take temperature input from the user
temperature = float(input("Enter the temperature in °C: "))

if temperature > 30:
    print("The temperature is too high")
elif temperature > 15:
    print("Normal temperature")
else:
    print("Cold temperature")



# Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true
# , print "Conditions met", otherwise print "Conditions not met"
x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))

if 10 <= x <= 20 and y > 100:
    print("Conditions met")

else:
    print("Conditions not met")

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is,
# print "Access   granted", otherwise print "Access denied"
password = input("Enter your password: ")
if password == "secret123":
    print("access granted")
else:
    print("access dinied")

#  5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student",
# otherwise print "Good score, but attendance needs improvement"  

  




