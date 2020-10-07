#Dang Nguyen
#ID 1861688

#6.17 CIS 2348 LAB: Password modifier (Zylab)

word = input()
password = ''


for x in word:
    if(x=='i'):
        password+="!"
    elif(x=='a'):
        password += "@"
    elif (x == 'm'):
        password += "M"
    elif (x == 'B'):
        password += "8"
    elif (x == 'o'):
        password += "."
    else:
        password += x
password += "q*s"
print(password)