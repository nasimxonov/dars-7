malumot = {"ism": "Saidnurmuhammadulloxon",                        
           "yosh": 18,                             
           "shahar": "Fergana"}                    
                                
try:                     
                    
    k = input("Keyni kiritng: ")                       
                                                      
    q = malumot[k]                            
                                                                   
    print(f"Value: {q}")                       
                            
except KeyError:                                                                         
                                                  
    print("Key mavjud emas")                      
                                               