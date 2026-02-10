#########one
password = input("Enter password: ")

if password == "admin123":
    print("Access Granted")
else:
    print("Access Denied")
#########two
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior")
########three
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Not Positive")

if num >= 10 and num <= 50:
    print("Between 10 and 50")
else:
    print("Not between 10 and 50")
########four
color = input("Enter a color: ")

if color != "":
    match color:
        case "red":
            print("Stop")
        case "yellow":
            print("Get Ready")
        case "green":
            print("Go")
        case _:
            print("Unknown color")
else:
    print("No input")
########five
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose an option (1-4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match choice:
    case "1":
        print("Result:", num1 + num2)
    case "2":
        print("Result:", num1 - num2)
    case "3":
        print("Result:", num1 * num2)
    case "4":
        print("Result:", num1 / num2)
    case _:
        print("Invalid option")
########six
score = int(input("Enter your score: "))

if score >= 60:
    print("Passed")
else:
    print("Failed")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")



