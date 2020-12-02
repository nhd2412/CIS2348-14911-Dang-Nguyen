# Dang Nguyen
# 1861688
# 12.7 CIS 2348 LAB: Fat-burning heart rate

def get_age():
    age = int(input())
    if not (age >= 18 and age <=75):
        raise ValueError('Invalid age.')
    return age


def fat_burning_heart_rate(age):
    heart_rate = (70/100) * (220 - age)
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, fat_burning_heart_rate(age) ))
    except ValueError as e:
        print(e)
        print('Could not calculate heart rate info.\n')
