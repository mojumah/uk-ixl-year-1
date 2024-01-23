name = input('Enter your father\'s name: ')
selector = int(input('Enter 1 to get nick name 1 or any other number to get nick name 2: '))
if selector == 1:
    sliced_name = name[2:8]
    print(sliced_name.capitalize())
else:
    sliced_name_two = name[0:2]
    print(sliced_name_two)