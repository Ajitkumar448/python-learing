def otp_verification (entered_otp,real_otp):
    if entered_otp == "":
        return"otp cannot be empty"
    if len(entered_otp) !=4:
             return"otp must have 4 digits"
    if entered_otp .isdigit():
            if entered_otp == real_otp:
             return"otp verified"
            else:
             return"otp verification is failed"
    else:
        return"otp must contain only digits"
    
entered_otp = (input("enter otp: "))
print(otp_verification(entered_otp,"1234"))
    
