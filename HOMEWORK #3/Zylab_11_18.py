#Dang Nguyen
#ID 1861688

input_list = [int(i) for i in input().split() if int(i) >= 0]
input_list.sort()
for number in input_list:
    print(number, end=" ")