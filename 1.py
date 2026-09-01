"""This Is Python Program Which Inputs Email And It Extracts Domain And
Username From It Also Checks Is It Ending With .com if ends With .com prints
True"""

email = input("Enter Your Email Address ")

# Extracting UserName
username = email.split("@")[0]
print(f"Username : {username.title()}")

# Extracting Domain
full_domain = email.split("@")[1]
domain = full_domain.split(".")[0]
print(f"Domain : {domain}")

# Extracting Extension And Checking is it .com
extension = full_domain.split(".")[1]
print(f"Extension : {extension}")

# Checking Whether It Ends With .com
print(f"Ends With .com? :{email.endswith('.com')}")
