import requests, os
from colorama import Fore, Style

oldprint = print
oldinput = input

def new_print(Section, Text):
  oldprint(f"{Fore.LIGHTBLUE_EX}${Fore.RESET} [{Fore.LIGHTCYAN_EX}{Section}{Fore.RESET}] * {Fore.WHITE}{Text}{Fore.RESET}")

def error(Section, Text):
  oldprint(f"{Fore.RED}${Fore.RESET} [{Fore.LIGHTRED_EX}{Section}{Fore.RESET}] * {Fore.WHITE}{Text}{Fore.RESET}")

def new_input(Section):
  return oldinput(f"{Fore.LIGHTMAGENTA_EX}%{Fore.RESET} [{Fore.LIGHTCYAN_EX}{Section}{Fore.RESET}] ..> ")

print = new_print
input = new_input

os.system("cls")
os.system("title "+ f"Capybara's Plug * Aged Amazon Account Generator")

print("Credits", "Capybara's Plug On Top")
print("Discord Server", "https://discord.gg/PXnm6UAK4x")
print("Mode (v.1)", "Aged Amazon Account Generator")

oldprint("")

ThreadMode = input("Threads (y/n)")

ThreadMode = ThreadMode.lower()

EmailsFile = open("./Files/Emails.txt", "r")

EmailAmount = 0 
Emails = ""

for Value in EmailsFile.readlines():
  EmailAmount = EmailAmount + 1
  Value = str(Value.rsplit())
  Value = str.replace(Value, "['", "")
  Value = str.replace(Value, "']", "")
  
  if EmailAmount == 1:
    Emails = f"{Value}"
  else:
    Emails = f"{Emails}:{Value}"

oldprint("")

print("Scanning", f"{EmailAmount} Accounts")

def exists(base, string):
  if string in base:
    return True

  return False

Session = requests.session()

targetUrl = "https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2FFoowin-Portable-Monitor-Display-Speaker%2Fdp%2FB09997HB8T%2Fref%3Dnav_ya_signin%3Fdchild%3D1%26keywords%3Dgaming%2Blaptops%26pf_rd_i%3D23508887011%26pf_rd_m%3DATVPDKIKX0DER%26pf_rd_p%3D434db2ed-6d53-4c59-b173-e8cd550a2e4f%26pf_rd_r%3D13Z0BD0XB6XMP1VGVWHM%26pf_rd_s%3Dmerchandised-search-5%26pf_rd_t%3D101%26qid%3D1628115073%26sr%3D8-1-spons%26psc%3D1%26spLa%3DZW5jcnlwdGVkUXVhbGlmaWVyPUEyMVpSV0NPVTc0Vk8xJmVuY3J5cHRlZElkPUEwMjg5MjY1MVRaVTczRUhaRjRQMCZlbmNyeXB0ZWRBZElkPUEwNzg5MzU3M0VJQTY5QUcwUDBQNyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&prevRID=8FM5Q6W6QSF4FQFKHA7P&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"

Session.get(targetUrl, headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"})

def check(email):
  request = Session.post(targetUrl, headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}, data = {"customerName": "Alex Gay", "email": email, "password": "Selexity123@", "passwordCheck": "Selexity123@"})

  if "account already exists" in request.text:
    return True

  return False

Checked = 0

for Email in Emails.split(":"):
  Success = check(Email)

  if Success:
    Checked = Checked + 1
    
    print("Hit", Email)
  else:
    error("Pass", Email)

oldprint("")

print("Total Hits", Checked)