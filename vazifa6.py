import random as r                       
                                    

with open("nimadir.txt", mode="w+") as file:                
    file.write(' '.join([str(r.randint(1, 20)) for x in range(10)]))              
                                                                
with open("nimadir.txt", mode="r") as file:                  
    text = file.read().split()

    text = map(int, text)


    text = list(filter(lambda x: x % 2 == 0, text))
                                                                              
with open("juft.txt", mode = "w+") as file2: 
    file2.write(' '.join(map(str, text)))
