# Dang Nguyen
# 1861688
# 12.9 CIS 2348 LAB: Exception handling to detect input string vs. integer

parts = input().split()
name = parts[0]
age = parts[-1]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except:
        age = 0
        print('{} {}'.format(name, age))
        
    
    parts = input().split()
    name = parts[0]