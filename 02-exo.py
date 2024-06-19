#
passWord = 'testpassword'
user_name = 'william'
input_password = input('Please enter your password ... : ')
input_user_name = input('Please enter your user name ... : ')
message =  print("Please enter the correct password and correct user name :( ")

while passWord  != input_password and user_name != input_user_name:
  input_password = input('Please enter your password ... : ')
  input_user_name = input('Please enter your user name ... : ')
  if(passWord != input_password or user_name != input_user_name):
    message
    
if passWord == input_password and input_user_name == user_name:
    print(f"Welcome {user_name}, you logged successfully :)")

  