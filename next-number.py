series = []

n = int(input("Enter number of elements : "))

for i in range (n):
    element = int(input("Enter number:"))
    series.append(element)

print(series)

last_number = series[-1]
print("Enter the number that comes after")
print (last_number)
answer = int(input("Enter your answer:"))
validate = answer - last_number

if (validate == 1):
    print('correct')
else:
    print('wrong')
