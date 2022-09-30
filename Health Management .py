print("\n\t\tWELCOME TO HEALTH MANANGEMENT SOFTWARE ccJustCodingWithVivek")

def getdate():
    import datetime
    l=str([str(datetime.datetime.now())])
    return l
try:
    print("\n\t\tPress 'l' to log tha data\n\t\tPress 'r' to retrieve tha data\n\t\tPress any key to exit")
    choice = input("What do you want ?? ")
    if choice == 'l':
        def log():
            print("\n\t\tPress 1 for Sumit\n\t\tPress 2 for Sushant\n\t\tPress 3 for Badal\n\t\tEnter any number to exit from the health management\n\t\tccJustCodingWithVivek")
            name=int(input("Enter the id of the patient: "))
        
           
            if name==1:
                
                print("\n\t\tPress 4 for Diet plan\n\t\tPress 5 for Exercise schedule")
                c=int(input("Enter your choice: "))
                
                if c==4:
                    with open("Sumit_diet.txt","a+") as f:
                        x=input("Mention today's diet of Sumit\n")
                        f.write(str(getdate())+"  "+x+"\n")
                        print("Content has been logged successfully")
               
                elif c==5:
                   with open("Sumit_exercise.txt","a+")as f:
                       x=input("Mention today's exercise done by Sumit\n")
                       f.write(str(getdate())+"  "+x+"\n")
                       print("Content has been logged successfully")
                       
                else:
                   print("Invalid input!!\nTry again")
                   

            elif name==2:
                
                print("\n\t\tPress 4 for Diet plan\n\t\tPress 5 for Exercise schedule")
                c=int(input("Enter your choice: "))
                
                if c==4:
                     with open("Sushant_diet.txt","a+") as f:
                         x=input("Mention today's diet of Sushant\n")
                         f.write(str(getdate())+"  "+x+"\n")
                         print("Content has been logged successfully")
                         
                elif c==5:
                    with open("Sushant_exercise.txt","a+")as f:
                        x=input("Mention today's exercise done by Sushant\n")
                        f.write(str(getdate())+"  "+x+"\n")
                        print("Content has been logged successfully")
                        
                else:
                    print("Invalid input\nTRY AGAIN!!!")
                    

            elif name==3:
                
                print("\n\t\tPress 4 to update Diet plan\n\t\tPress 5 to update Exercise schedule")
                c=int(input("Enter your choice: "))
                
                if c==4:
                    with open("Badal_diet.txt","a+") as f:
                        x=input("Mention today's diet of Badal\n")
                        f.write(str(getdate())+"  "+x+"\n")
                        print("Content has been logged successfully")
               
                elif c==5:
                   with open("Badal_exercise.txt","a+")as f:
                       x=input("Mention today's exercise done by Badal\n")
                       f.write(str(getdate())+"  "+x+"\n")
                       print("Content has been logged successfully")
               
                else:
                    print("Invalid input\nTRY AGAIN!!!")     
        log()  
        
          #ccJustCodingWithVivek
    elif choice == 'r':
        def retrieve():
            print("\n\t\tPress 1 for Sumit\n\t\tPress 2 for Sushant\n\t\tPress 3 for Badal\n\t\tEnter any number to exit from the health management\n\t\tccJustCodingWithVivek")
            name=int(input("Enter the id of the patient: "))
            
            if name==1:
                
                print("\n\t\tPress 4 to retrieve Diet plan\n\t\tPress 5 to retrieve Exercise schedule")
                c=int(input("Enter your choice: "))
                
                if c==4:
                    with open("Sumit_diet.txt") as f:
                        r=f.read()
                        if r=="":
                            print("No content available")
                        else:
                            print(r)
                        
                
                elif c==5:
                   with open("Sumit_exercise.txt")as f:
                       r=f.read()
                       if r=="":
                           print("No content available")
                       else:
                           print(r)
                else:
                    print("Invalid input!!\nTry again")
                    
              #ccJustCodingWithVivek        
            elif name==2:
                
                print("\n\t\tPress 4 to retrieve Diet plan\n\t\tPress 5 to retrieve Exercise schedule")
                c=int(input("Enter your choice: "))
                
                if c==4:
                    with open("Sushant_diet.txt") as f:
                        r=f.read()
                        if r=="":
                            print("No content available")
                        else:
                            print(r)
                
                elif c==5:
                   with open("Sushant_exercise.txt")as f:
                       r=f.read()
                       if r=="":
                           print("No content available")
                       else:
                           print(r)
                       
            
                else:
                    print("Invalid input!!\nTry again")
              
                    
            elif name==3:
                
                print("\n\t\tPress 4 to retrieve Diet plan\n\t\tPress 5 to retrieve Exercise schedule")
                c=int(input("Enter your choice: "))
                
                if c==4:
                    with open("Badal_diet.txt") as f:
                        r=f.read()
                        if r=="":
                            print("No content available")
                        else:
                            print(r)
                        
                 #ccJustCodingWithVivek 
                elif c==5:
                   with open("Badal_exercise.txt")as f:
                       
                       r=f.read()
                       if r=="":
                           print("No content available")
                       else:
                           print(r)
                       
                else:
                    print("Invalid input!!\nTry again")            
        retrieve()

    else:
        print("Successfully Exit!!!")

       #ccJustCodingWithVivek
except Exception as e:
    print(e)  
