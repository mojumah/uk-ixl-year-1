StartNumber = int(input("Enter 0 or 1: "))

if ((StartNumber != 0) and (StartNumber != 1)):
    print('Enter 0 or 1')

else:

    EndNumber = int(input("Enter number you want to reach: "))

    while StartNumber < EndNumber:

        StartNumber += 1
        print(StartNumber)