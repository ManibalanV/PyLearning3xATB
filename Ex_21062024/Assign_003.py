# Programming Question
#
# Ctrl + / for making notes
# ✅ Right Triangle Star Pattern
#
total_rows = int(input("Enter the number of rows: "))

for row in range(1, total_rows+1):
    # Display Star:
    for symbol in range(1, row+1):
        print("*", end="")
    print()

# *
# **
# ***
# ****
# *****
# ----------------------------------------------------------------
#
# ✅ Palindrome of String

name = input("Enter the name to check the palindrom: ")
rev_name = name[::-1]

if name == rev_name:
    print('true')
else:
    print('false')
#
#
# i/p = naman , nitin, level
#
# o/p = true
#
#
#
# i/p = pramod
#
# o/p = false
#
#
#
#
# ----------------------------------------------------------------
# ✅ String Reverse
#
#
# Method 1: Using string functions
name = input("Enter the string to reverse it using Method 1: ")
rev_name = name[::-1]
print(rev_name)
print("----------------------------------")
# Method 2: Using empty string and for loop
name = input("Enter the string to reverse it using Method 2: ")
rev_name = ""

for char in name:
    rev_name = char+rev_name

print(rev_name)

print("----------------------------------")
# Method 3: Using while loop
name = input("Enter the string to reverse it using Method 3: ")
rev_name = ""
length = len(name)-1
while length >= 0:
    rev_name = rev_name + name[length]
    length = length - 1

print(rev_name)
#
# 3-4 ways to do this in Python
#
#
#
# ----------------------------------------------------------------
# ✅ Count vowels and consonants in a String
word = input("Enter any word to count the vowels and consonants: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count_vowels = 0
count_consonant = 0
for i in word:
    if i in vowels:
        count_vowels += 1
    else:
        count_consonant += 1

print("Vowels count is", count_vowels)
print("Consonant count is", count_consonant)
#
# ----------------------------------------------------------------
# ✅ Anagrams

word1 = input("Enter word 1 to check anagram: ")
word2 = input("Enter word 2 to check anagram: ")
sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)

if sorted_word1 == sorted_word2:
    print("Anagram")
else:
    print("Not anagram")


# String s1 = "silent";
#
# String s2 = "listen";
#
#
#
# namo - mano - onam
#
#
#
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase
# ----------------------------------------------------------------