import random
import string 

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = "!@#$%^&*()"

all_combined  = uppercase + lowercase + digits + special


total_password_length =  int(input("Enter length of password: "))
total_length = len(all_combined)
password = ""
for i in range(total_password_length):
    random_numebr = random.randint(0, total_length - 1) #71
    password += all_combined[random_numebr] #fc)

print(f"Your password is: \n{password}")

# 