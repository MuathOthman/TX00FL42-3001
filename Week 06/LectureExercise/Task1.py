seasons = ("Winter", "Spring", "Summer", "Autumn")

month_num = int(input('Enter a month number 1-12: '))

if month_num < 3 or (13 > month_num > 11):
    print(seasons[0])
elif 2 < month_num < 6:
    print(seasons[1])
elif 5 < month_num < 9:
    print(seasons[2])
elif 8 < month_num < 12:
    print(seasons[3])
else:
    print('Error. Try again from 1 to 12.')