"""
#------------------Kiasoft Internship------------------#
| Name :- Sagar Parmar                                 |
| Intern ID :- CR660                                   |
| Project Name :- OTP Generator (Console Application)  |
#------------------------------------------------------#
"""
import random
import string

def pwd_size(size_of_digit):
    digit_pwd=''.join([random.choice(string.digits)for digit in range(size_of_digit)])    
    return digit_pwd 
create_otp = pwd_size(4)
print(f'Your OTP is : {create_otp}')

while True:
    OTP = input('Enter your OTP Here :')
    if OTP == create_otp:
        print('Your OTP is Valid')
        break
    
    else:
        print('invalid OTP, Please Enter Correct OTP')
        continue