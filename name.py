from PIL import Image
img = Image.open("./fruits/watermelon.png")
img.show()

answer = input("What is the name of this fruit ?")
if answer == 'watermelon':
    print('correct')
elif answer == 'Watermelon':
    print('correct')
elif answer == ('جبسة'):
    print('correct')
elif answer == ('بطيخة'):
    print('correct')
elif answer == ('حبحب'):
    print('correct')
else:
    print('wrong')