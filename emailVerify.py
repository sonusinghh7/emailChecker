space, Capital, smb = 0, 0, 0                                   
email= input ("Enter your Email here: ")                        
if len(email) >=6:                                              
    if email[0].isalpha() :                                     
        if ('@' in email) and (email.count('@')==1):            
            if (email[-4]=='.') ^ (email[-3]=='.'):             
                for i in email:                                 
                    if i == i.isspace():                        
                        space = 1                               
                    elif i.isalpha() or i.isdigit:              
                        if i==i.upper():                        
                            capital = 1                         
                    elif i == '_' or '.' or i == '@':           
                        continue                                
                    else:                                       
                        smb  = 1                                
                if space == 1 or Capital == 1 or smb == 1:      
                        print("Enter the valid email")          
                else:                                           
                    print("Email verification successfully...") 
            else:                                               
                print("Please enter the valid email")           
        else:                                                   
            print("Enter the valid email")                      
    else:                                                       
        print("Please enter the valid email")                   
else:                                                           
    print("Please enter valid email")                            