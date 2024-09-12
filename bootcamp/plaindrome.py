word = input('Enter the word you want to test: ')
print(word)
reverse = word[::-1]
if word == reverse:
    print('This word is a plaindrome')
else:
    print('This word is not a plaindrome')