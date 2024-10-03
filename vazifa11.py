try:
                                           
    filee = input("File nomini kiriting: ")                
                                                            
    with open(filee, 'r') as file:                                 
                                                            
        f = file.read()                           
                   
        print(f)                                
                                       
except FileNotFoundError:               
                             
    print("Fayl topilmadi🤷🏻‍♂️")                        
