# Multiple conditions

# Switch in Java
# If elif else: we can use.. In python instead of "switch" we have "match"
# above 3.10 version "match" function will work

numbers = int(input("Enter the number: \n"))

match numbers:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case 6:
        print("You have entered 6")
    case _:
        print("No Idea")

print("====================================")

browser = str(input("Enter the browser name: \n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed!")
    case "firefox":
        print("Firefox code executed!")
    case _:
        print("No browser found!")

