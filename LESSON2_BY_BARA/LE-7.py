# CLEAN THE CASES >> lower() & upper() CASE CONVERSION

# text = "python PROGRAMMING"
# print(text.lower())
# print(text.upper())


search = "Email"
data = "email"
print(search == data)

search = " Email  ".lower().strip()
data = "  email ".lower().strip()
print(search == data)


#best practice -- CLEAN BEFORE SEARCH


#PYTHON CHALLENGE -- CLEAN THE DATA  

#"968-Maria, ( D@t@ Engineer );; 27y  " get >> name: maria | role: data engineer | age: 27

emp_data = "968-Maria, ( D@t@ Engineer );; 27y  "
name = emp_data.replace("968-" , "name: ").replace("," , "| role:").replace("(" , "").replace(")" , "").replace("D@t@" , "Data").replace(";;" , "| age:").replace("y" , "").lower().strip();
print (name)