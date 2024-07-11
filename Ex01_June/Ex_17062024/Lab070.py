# Factorial
n = 5
factorial = 1

for i in range(1, n+1):
    factorial = factorial * i

print("For Loop method", factorial)

# factorial = 1
# range(1, 5+1) # range(1, 6) # 1, 2, 3, 4, 5

# Note : factorial = factorial * i
# when i = 1 : factorial = factorial * i # factorial = 1 * 1 = 1
# when i = 2 : factorial = factorial * i # factorial = 1 * 2 = 2 # Now variable factorial becomes 2 and stored in variable factorial
# when i = 3 : factorial = factorial * i # factorial = 2 * 3 = 6 # Now variable factorial becomes 6 and stored in variable factorial
# when i = 4 : factorial = factorial * i # factorial = 6 * 4 = 24 # Now variable factorial becomes 24 and stored in variable factorial
# when i = 5 : factorial = factorial * i # factorial = 24 * 5 = 120
# Loop ends



x = 5
factoria = 1

while x>0:
    factoria = factoria*x
    x = x-1

print("while loop method", factoria)

# Note : factoria = factoria * x
# when x = 5 : factoria = factoria * x # factoria = 1 * 5 = 5
# when x = 4 : factoria = factoria * x # factoria = 5 * 4 = 20 # Now variable factorial becomes 2 and stored in variable factorial
# when x = 3 : factoria = factoria * x # factoria = 20 * 3 = 60 # Now variable factorial becomes 6 and stored in variable factorial
# when x = 2 : factoria = factoria * x # factoria = 60 * 2 = 120 # Now variable factorial becomes 24 and stored in variable factorial
# when x = 1 : factoria = factoria * x # factoria = 120 * 1 = 120
# when x = 0 : while 0 > 0: condition false: out of the loop
# Loop ends




