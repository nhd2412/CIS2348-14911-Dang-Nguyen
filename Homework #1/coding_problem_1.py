# Dang Nguyen
# ID 1861688
# Coding Problem 1

print('Birthday Calculator\nCurrent day')
user_current_month = int(input('Month: '))
user_current_day = int(input('Day: '))
user_current_year = int(input('Year: '))
print("Birthday")
user_birthday_month = int(input('Month: '))
user_birthday_day = int(input('Day: '))
user_birthday_year = int(input('Year: '))

if user_current_day < user_birthday_day and user_current_month < user_birthday_month:
    user_age = user_current_year - user_birthday_year - 1

if user_current_day < user_birthday_day and user_current_month == user_birthday_month:
    user_age = user_current_year - user_birthday_year - 1

if user_current_day < user_birthday_day and user_current_month > user_birthday_month:
    user_age = user_current_year - user_birthday_year

if user_current_day == user_birthday_day and user_current_month < user_birthday_month:
    user_age = user_current_year - user_birthday_year - 1

if user_current_day == user_birthday_day and user_current_month == user_birthday_month:
    user_age = user_current_year - user_birthday_year
    print("Happy Birthday!")

if user_current_day == user_birthday_day and user_current_month > user_birthday_month:
    user_age = user_current_year - user_birthday_year

if user_current_day > user_birthday_day and user_current_month < user_birthday_month:
    user_age = user_current_year - user_birthday_year - 1

if user_current_day > user_birthday_day and user_current_month == user_birthday_month:
    user_age = user_current_year - user_birthday_year

if user_current_day > user_birthday_day and user_current_month > user_birthday_month:
    user_age = user_current_year - user_birthday_year

print('Your are {} years old.'.format(user_age))