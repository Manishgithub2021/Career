import random
collections_caps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
collections_small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
collections_symbol=['!','@','#','$','%','^','&','*','(',')',',',':','/']
#print(collections_symbol[len(collections_symbol)-1])
while(True):
    length_of_password=int(input("Enter length of password required  "))
    how_many_caps=int(input("Enter how many caps letter you want  "))
    how_many_small=int(input("Enter how many small letter you want  "))
    how_many_symbol=int(input("Enter how many symbols you want  "))
    if (how_many_caps+how_many_small+how_many_symbol)!=length_of_password:
        print("Check your combinations")
    else:
        password_list=[]
        yourpassword=""
        for i in range(how_many_caps):
            letter=random.choice(collections_caps)
            password_list.insert(i,letter)

        for i in range(how_many_small):
            letter=random.choice(collections_small)
            password_list.insert(how_many_caps+i,letter)

        for i in range(how_many_symbol):
            letter=random.choice(collections_symbol)
            password_list.insert(how_many_caps+how_many_small+i,letter)


        random.shuffle(password_list)

        for x in password_list:
            yourpassword+=x
        print(f"Your {length_of_password} digit password is {yourpassword}  ")
    wanttocontinue=input("To generate more password enter Y ,to exit enter N  ").lower()
    if wanttocontinue=='n':
        break
        
    
    
        
        
            
    



