import random
days = ["Monday", "Tuesday", "Wednesday" ,"Thursday", "Friday", "Saturday", "Sunday"]
random.shuffle(days)
random_day = days[-1]
print("Enter the day that comes after")
print(random_day)
answer = input("Enter your answer: ")

if ((random_day == "Monday") and (answer == "Tuesday")):
    print('correct')
elif((random_day == "Tuesday") and (answer == "Wednesday")):
    print('correct')
elif((random_day == "Wednesday") and (answer == "Thursday")):
    print('correct')
elif((random_day == "Thursday") and (answer == "Friday")):
    print('correct')
elif((random_day == "Friday") and (answer == "Saturday")):
    print('correct')
elif((random_day == "Saturday") and (answer == "Sunday")):
    print('correct')
elif((random_day == "Sunday") and (answer == "Monday")):
    print('correct')
else:
    print('wrong')