letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'd', 'e', 'i', 'j', 'o', 'u')
letters_set = {'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}

# Filter the vowels : a e i o u

def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


result = filter_vowels('a')
print(result)

filtered_words = filter(filter_vowels, letters)
print(list(filtered_words))

filtered_words = filter(filter_vowels, letters_set)
print(list(filtered_words))

filtered_words = filter(filter_vowels, letters_tuple)
print(list(filtered_words))