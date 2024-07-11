# Format String

print(2*1)
num = 90
print(f'The number is {num*3}')


#By using string formating we can print the multiplication table as well
num = 9
print(f'{num}x1={num}')
print(f'{num}x2={num*2}')
print(f'{num}x3={num*3}')
print(f'{num}x4={num*4}')
print(f'{num}x5={num*5}')
print(f'{num}x6={num*6}')
print(f'{num}x7={num*7}')
print(f'{num}x8={num*8}')
print(f'{num}x9={num*9}')
print(f'{num}x10={num*10}')

#name = Manibalan
#name2 = Sivabalan
print("Hello my name is {name} {name2} ".format(name = "Manibalan" , name2 = "Sivabalan"))
print("Hello my name is {0} {1} ".format("Manibalan" , "Sivabalan"))
print("Hello my name is {} {} ".format("Manibalan" , "Sivabalan"))
print("Hello my name is {1} {0} ".format("Manibalan" , "Sivabalan"))

"""
Formatting Types
Inside the placeholders you can add a formatting type to format the result:

:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
"""

