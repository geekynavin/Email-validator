import re
s=input("Enter email id:")
m=re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com',s)
if m!=None:
	print("Verified !!")
else:
	print("Please enter the valid email id")