# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = input('Enter your palindrome word: ')
word = str(word)
rev = word[::-1]
print(rev)

if rev == word:
    print('This is a palindrome sentence')
else:
    print("This is not a palindrome sentence")


##### Second method of doing this example.

name = input('again Enter your phrase so that I tell you that it si palindrome or not:  ')

if name[::-1] == name[0:]:
    print('Yes! This is a palindrome sentence.')
else:
    print('This is not a palindrome sentence.')