# membership operators IN, and NOT IN  condition search for a value in a list or a string

print("f" not in "python") #// output will be true because the condition is false and we are reversing it
print("f" not in "fox") #// output will be false because the condition is true and we are reversing it

#USE CASE
# Security check: ensure the domain is not banned

domain = "gmail.com"
banned_domains = ["span.com", "yahoo.com", "hotmail.com"]
print(domain not in banned_domains) 