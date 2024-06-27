# Break
# Break is used to escape the loop when the condition is not met.
# Here's a concrete example.

# Python does not have a built-in do-while loop structure that you might find in other programming languages like C++ or Java.

# For Loop

for counter in range(0, 100): #0 to 99
    print(counter)

for counter2 in range(0, 101, 2): #Even
    print(counter2)

for counter3 in range(1, 100, 2): #Odd
    print(counter3)

for counter4 in range(1, 101):
    print(counter4)
    if counter4 == 5:
        break
print("Outside of the program")

