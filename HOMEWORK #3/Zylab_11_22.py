#Dang Nguyen
#ID 1861688

list = input()
text = list.split()
for word in text:
        freq = text.count(word) 
        print(word, freq)