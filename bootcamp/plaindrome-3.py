list = []
plaindrome = []
normal = []

x = 0
y = int(input("Enter the number of words you want to test if they are plaindromes or not: "))
while x < y:
    x = x + 1
    word = input("Enter the word number " + str(x) + ": ")
    word_reversed = word[::-1]
    if word == word_reversed:
        plaindrome.append(word_reversed)
    else:
        normal.append(word)

print("the list of plaindrome words are " )
print(plaindrome)
print("the list of normal words are ")
print(normal)