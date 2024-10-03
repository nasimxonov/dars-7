matn = input("Nimadir kiriting: ")                 
                            
with open("nimadir.txt", mode="w+") as file:
    file.write(matn)                                                   
                                               
with open("nimadir.txt", mode="r") as file:                  
    text = file.readlines()                               
                                                      
teskari_text = [i.strip()[::-1] for i in text]                   
                                                   
with open("teskari.txt", mode = "w") as file2:                  
                                                
    for i in teskari_text:                                
                                         
        file2.write(i + '\n')           
                                    
                                         