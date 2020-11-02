# Dang Nguyen
#ID 1861688

def print_menu():
    print("\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n"
          "r - Output players above a rating\no - Output roster\nq - Quit\n")

def add_player():        
    while True:
        print("\nEnter a new player's jersey number:",end="")        
        jersey_num=int(input())        
        if jersey_num>=0  and jersey_num<=99:                            
            break        
        else:           
            print("wrong value enterted!! Enter the rating between 0-99")    
            
    while True:        
        print("Enter the player's rating:",end="")        
        rating=int(input())        
        if rating>=0  and rating<=9:                           
            break      
        else:       
            print("wrong value enterted!! Enter the rating between 0-9")    
            
    my_dict[jersey_num]=rating         
            
def add5Players():   
    for i in range(5):      
        while True:          
            print("Enter player "+str(i+1)+"'s jersey number:",end="")      
            jersey_num=int(input())         
            if jersey_num>=0  and jersey_num<=99:              
                break        
            else:          
                print("wrong value enterted!! Enter the rating between 0-99")    
                                
        while True:     
            print("\nEnter player "+str(i+1)+"'s rating:",end=""'\n\n')     
            rating=int(input())        
            if rating>=0  and rating<=9:                
                break         
            else:        
                 print("wrong value enterted!! Enter the rating between 0-9")            
                 
        my_dict[jersey_num]=rating

def remove_player():    
    print("\nEnter a jersey number: ",end="")    
    jersey_num=int(input())    
    del my_dict[jersey_num]

def output_roster():
    print("ROSTER")    
    for key,value in sorted(my_dict.items()):        
        print("Jersey number: {}, Rating: {}".format(key, value))

def update_player():    
    while True:        
        print("\nEnter a jersey number:",end="")        
        jersey_num=int(input())        
        if jersey_num in my_dict.keys():            
            break        
        else:            
            print("Entered jersey number is not present. Please select another one.")    
    while True:        
        print("Enter a new rating for player:",end="")        
        rating=int(input())        
        if rating>=0  and rating<=9:                           
            break        
        else:            
            print("wrong value enterted!! Enter the rating between 0-9")    
                        
    my_dict[jersey_num]=rating
    
def above_rating_players():    
    print("\nEnter a rating: ",end="")    
    rating=int(input())   
    print("ABOVE",rating)    
    for value in sorted(my_dict, key=my_dict.get, reverse=True):        
        if value>rating:           
            print("Jersey number: {}, Rating: {}".format(my_dict[value],value))
my_dict={}
def main():    
    add5Players()    
    output_roster()    
    print_menu()    
    ch=input("Choose an option:\n")
main()