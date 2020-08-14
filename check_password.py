import re

def check_password(password):
    phone = re.compile(r"[a-zA-Z(\d)+]{8,}")
    if phone.match(password):
        print("Correct!")
    else:
        print("Not accepted!")
        
        
check_password("ayodabo2")