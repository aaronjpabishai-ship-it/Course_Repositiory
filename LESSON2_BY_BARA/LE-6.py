#CLEANING DATA.

#EMOVING WHITESPACES from the lesft side 
# text = " engineering".lstrip()
# print(text)

#from the right sude
# text = "engineering ".rstrip()
# print(text)

# #from both sides
# text = " engineering ".strip()
# print(text)

#CALCULATING LENGTH OF A STRING
text = "PHOTOGRAPHY"
print(len(text)) #will calculate the length of the string including the whitespace
print(len(text.strip())) #will remove the whitespace and calculate the length of the string

#### professionally check if your dtata has any white spaces
nr_of_whtspaces = len(text) - len(text.strip())
is_clean =  len(text) == len(text.strip())
print(nr_of_whtspaces)
print(is_clean)