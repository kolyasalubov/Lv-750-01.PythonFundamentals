LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
HIGH_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
NUMBERS = "0123456789"
CHR = "!@#$%^&*~`:;?"

l,h,p,n = 0, 0, 0, 0                      
user_password = input("Pass your password:") 
if len(user_password) > 6 or len(user_password) < 16:
    
    for i in user_password:
        if i in LOWER_LETTERS:
            l += 1
        elif i in HIGH_LETTERS:
            h += 1
        elif i in NUMBERS:
            n += 1
        elif i in CHR:
            p += 1
if (l >= 1 and h >= 1 and n >= 1 and p >= 1 and l+h+n+p == len(user_password)):
    print("Valid password")
else:
    print("Invalid password")                           
    
                        
        


