#P-Word | Password Generator by Lolopold_
#I'm still learning to code and I'd love to hear your feedback or even recomendations.
#This is my programming journey
#I hope someone can use this
#XOXO
#
#	  _ \    \ \        /             | 
#	 |   |    \ \  \   / _ \   __| _` | 
#	 ___/_____|\ \  \ / (   | |   (   | 
#	_|          \_/\_/ \___/ _|  \__,_| 
#

import random
import colorama
from colorama import Fore, Style

print(Fore.RED +"Welcome to the P-Word | Password Generator. This is version 2.0 \n")
print(Style.RESET_ALL)

#inputs of user
password_len = int(input("How Long Should Your Password Be?	"))
password_type = int(input("""\n \n What Should Be Included In Your Password? \n
1. Lowercase \n
2. Uppercase \n
3. Numbers \n
4. Special Characters \n \n
[1, 2, 3, 4]:	"""))

if password_type not in (1,2,3,4,12,13,14,123,134,1234,124,23,24,234,34):
	print("\n \n Wrong Order Of Numbers Or Number(s) Not In Range (1-4).")

else:
	safe = int(input("\n Do You Want To Safe The Password In A File? [0,1]:	"))


#lists of the password types
num = [1,2,3,4,5,6,7,8,9,0]
let = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
LET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chr = ["@","!","§","$","%","&","=","?","|","+","*","-","_","^"]


#check the input of user
if password_type == 1234 :
	comb_list = let + LET + num + chr;

if password_type == 1:
	comb_list = let
	
if password_type == 12:
	comb_list = let + LET;

if password_type == 13:
	comb_list = let + num

if password_type == 14:
	comb_list = let + chr

if password_type == 123:
	comb_list = let + LET + num

if password_type == 134:
	comb_list = let + num + chr

if password_type == 124:
	comb_list = let + LET +chr
	
if password_type == 2:
	comb_list = LET

if password_type == 23:
	comb_list = LET + num

if password_type == 24:
	comb_list = LET + chr

if password_type == 234:
	comb_list = LET + num + chr

if password_type == 3:
	comb_list = num

if password_type == 34:
	comb_list = num + chr

if password_type == 4:
	comb_list = chr
	
password_rand = random.choices(comb_list, k=password_len);
password = ''.join(str(list)for list in password_rand)
print("\n")
print(Fore.GREEN + password)
print(Style.RESET_ALL)
if safe == 1:
	with open("password.txt", "w") as external_file:
		add_text = password
		print(password, file=external_file)
		external_file.close()
		print("Your Password Is Now Safed As password.txt In Your Home Directory")
else:
	print("\n You Can Now Copy Your Freshly New Generated Password")
#be polite and say bye!
print("\n \n Ok, Bye...")
