#Secure Password Generator by Lolopold_
#I'm still learning to code and I'd love to hear your feedback or even recomendations.
#This is my programming journey
#I hope someone can use this
#XOXO
#
#  _ \                                        |   ___|                           |              
# |   | _` |  __|  __|\ \  \   / _ \   __| _` |  |      _ \ __ \   _ \  __| _` | __|  _ \   __| 
# ___/ (   |\__ \\__ \ \ \  \ / (   | |   (   |  |   |  __/ |   |  __/ |   (   | |   (   | |    
#_|   \__,_|____/____/  \_/\_/ \___/ _|  \__,_| \____|\___|_|  _|\___|_|  \__,_|\__|\___/ _| 


import random


#inputs of user
password_len = int(input("How Long Should Your Password Be?	"))
password_type = int(input("""\n \n \n What Should Be Included Yn Your Password? \n
1. Lowercase \n
2. Uppercase \n
3. Numbers \n
4. Special Characters \n \n
[1, 2, 3, 4]:	"""))


#lists of the password types
num = [1,2,3,4,5,6,7,8,9,0]
let = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
LET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chr = ["{","}","[","]","@","!","§","$","%","&","/","(",")","=","?","`"]


#check the input of user
if password_type == 1234 :
	comb_list = let + LET + num + chr;
	password_rand = random.choices(comb_list, k=password_len);
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 1:
	comb_list = let
	password_rand = random.choices(comb_list, k=password_len);
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 12:
	comb_list = let + LET;
	password_rand = random.choices(comb_list, k=password_len);
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 13:
	comb_list = let + num
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 14:
	comb_list = let + chr
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 123:
	comb_list = let + LET + num
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 134:
	comb_list = let + num + chr
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 124:
	comb_list = let + LET +chr
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 2:
	comb_list = LET
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 23:
	comb_list = LET + num
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 24:
	comb_list = LET + chr
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 234:
	comb_list = LET + num + chr
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 3:
	comb_list = num
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password)
if password_type == 34:
	comb_list = num + chr
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password) 
if password_type == 4:
	comb_list = chr
	password_rand = random.choices(comb_list, k=password_len)
	password = ''.join(str(list)for list in password_rand)
	print(password) 


#be polite and say bye!
else:
	print("\n \nOk, Bye...")
