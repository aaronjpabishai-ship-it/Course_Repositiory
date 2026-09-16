# TRANSFORMATION 


#replace() replacing the value of specific data

# price = "1234,56"
# print(price.replace ("," , "."))


# phone = "254-456-879"
# print(phone.replace("-" , "_"))

# phone = "254-456-879"
# print(phone.replace("-" , ""))

# price = "$1,299.99"
# print(price.replace("$" , "").replace("," , "")) # chained method

#PYTHON CHALLENGE -- CONVERT "+49 (179) 123-456"

# phone = "+49(179)123-456"
# print(phone.replace("+" , "00").replace("(" , "").replace(")" , "").replace("-" , ""))

##joins()

# first_name = "Aaron"
# last_name = "Abishai"
# name = first_name + " " + last_name
# print(name)

folder = "F:/Users/aaronabishai/"
file =  "data.json"
full_file_path = folder + file
print(full_file_path)