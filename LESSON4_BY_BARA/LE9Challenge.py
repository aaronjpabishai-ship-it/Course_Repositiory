#CHALLENGE 9
#Check if the user name is not empty and the age is greater than or equal to 18
#Check if the password is atleast 8 characters long and does not contain spaces 
#Check if a users email is not empty, contains '@' and ends with '.com'
#Check is a user name is a string, is not None, and is longer than 5 characters
#Check if the user is either an admin or a moderator, and either ther're not banned or they've verified their email 

import string


username = "admin@gmail.com"
password = "Passwords7854"
age = 25
is_not_banned = True
user = "Admin"
user = username

print(username != "" and age >= 18)
print(len(password) >= 8 and " " is not password)
print(username != "" and "@" in username and username.endswith(".com"))
print(isinstance(username, str) and username is not None and len(username) > 5)
print(user == "Admin" or user == "Moderator" and (is_not_banned or username.endswith(".com") and user == username))