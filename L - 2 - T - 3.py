# LEVEL - 2

#TASK - 3 - Password Strength Checker

def check_password(password):
    
    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        
        if ch >= 'A' and ch <= 'Z':
            upper = True
            
        if ch >= 'a' and ch <= 'z':
            lower = True
            
        if ch >= '0' and ch <= '9':
            digit = True
            
        if ch in "!@#$%^&*":
            special = True

    if len(password) < 8:
        print("Password should contain more than 8 characters.")
        
    elif upper == False:
        print("Add uppercase letter")
        
    elif lower == False:
        print("Add lowercase letter")
        
    elif digit == False:
        print("Add number")
        
    elif special == False:
        print("Add special character")
        
    else:
        print("Password is strong")

pw = input("Enter your password: ")
check_password(pw)

