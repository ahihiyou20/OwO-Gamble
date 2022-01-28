import time
import os
from multiprocessing import Process
from multiprocessing import Pool
import random
import re
import atexit
if os.name == 'posix':
 try:
  import simplejson as json
 except:
  os.system('pip install simplejson')
  import simplejson as json
if os.name == 'nt':
  import json
try:
 import discum
except:
 if os.name == 'nt':
  os.system('py -m pip install -r requirements.txt')
 if os.name != 'nt':
  os.system('pip install -r requirements.txt')
 import discum
print("""\
░█████╗░░██╗░░░░░░░██╗░█████╗░  ░██████╗███████╗██╗░░░░░███████╗  ██████╗░░█████╗░████████╗
██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║░╚██╗████╗██╔╝██║░░██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║░░████╔═████║░██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝███████╗███████╗██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░

**Version: CoinFlip**""")
wbm=[14,16]
time.sleep(2)
class client:
  commands=[
    "t","h"
   ]
  bet = 1000
  totalcmd = 0
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    if os.name == "nt":
      purple = ''
      okblue = ''
      okcyan = ''
      okgreen = ''
      warning = ''
      fail = ''
      reset = ''
      bold = ''
      underline = ''
  with open('settings.json', "r") as file:
        data = json.load(file)
        token = data["token"]
        channel = data["channel"]
  if data["token"] and data["channel"] == 'nothing':
   print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
   time.sleep(1)
   if os.name == 'nt':
    os.system('py newdata.py')
   if os.name != 'nt':
    os.system('python newdata.py')
  print('=========================')
  print('|                       |')
  print(f'| [1] {color.purple}Load data         {color.reset}|')
  print(f'| [2] {color.purple}Create new data   {color.reset}|')
  print(f'| [3] {color.purple}Credit            {color.reset}|')
  print('=========================')
  time.sleep(1)
  time.sleep(1)
choice = int(input('Enter your choice: '))
if (choice == 1):
      pass
if (choice == 2):
     if os.name == 'nt':
      os.system('py newdata.py')
     if os.name != 'nt':
      os.system('python newdata.py')
if (choice == 3):
      print(f'{client.color.okcyan} =========Credit=========={client.color.reset}')
      print(f'{client.color.purple} [Developer] {client.color.reset} ahihiyou20')
      print(f'{client.color.okcyan} Someone just leave this project :( {client.color.reset}')
      time.sleep(5)
      exit() 
if (choice == 4):
 print(f'{client.color.purple} COMING SOON! {client.color.reset}')
 time.sleep(2)
 exit()
if not (choice ==1 or 2 or 3 or 4): 
 print(f'{client.color.fail} !! [ERROR] !! {client.color.reset} Wrong input!')
 time.sleep(2)
 exit()
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
bot = discum.Client(token=client.token, log=False)
@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
@bot.gateway.command
def issuechecker(resp):
 if resp.event.message:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel:
    if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
     if 'captcha' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      time.sleep(1)
      bot.gateway.close()
     if '(2/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (2/5)')
      time.sleep(1)
      bot.gateway.close()
     if '(3/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (3/5)')
      time.sleep(1)
      bot.gateway.close()
     if '(4/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (4/5)')
      time.sleep(1)
      bot.gateway.close()
     if '(5/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (5/5)')
      time.sleep(1)
      bot.gateway.close()
     if 'banned' in m['content']:
      print(f'{at()}{client.color.fail} !!! [BANNED] !!! {client.color.reset} your account have been banned from owo bot please open a issue on the Support Discord server')
      time.sleep(1)
      bot.gateway.close()
     if 'complete your captcha to verify that you are human!' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      time.sleep(1)
      bot.gateway.close()
     if 'DM' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      time.sleep(1)
      bot.gateway.close()
     if 'you currently have' in m['content']:
       issuechecker.cash = re.findall('[0-9]+', m['content'])
       print("{}You currently have: {}{} Cowoncy!{}".format(client.color.warning,issuechecker.cash[1],issuechecker.cash[2],client.color.reset))
@bot.gateway.command
def check(resp):
  if resp.event.message_updated:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel:
    if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
      if 'and you won' in m['content']:
       print("{}Won: {} Cowoncy{}".format(client.color.okgreen,client.bet*2,client.color.reset))
       client.bet = 1000
      if 'and you lost it all... :c' in m['content']:
       print("{}Lost: {} Cowoncy {}".format(client.color.fail,client.bet,client.color.reset))
       client.bet = client.bet*2
@bot.gateway.command
def cf(resp):
 if resp.event.ready:
  choice = random.choice(client.commands)
  bot.sendMessage(str(client.channel), "owo cf {} {} ".format(client.bet,choice))
  print("owo cf {} {}".format(client.bet,choice))
  client.totalcmd = client.totalcmd + 1
  time.sleep(random.randint(wbm[0], wbm[1]))
  bot.sendMessage(str(client.channel), "owo cash")
  time.sleep(random.randint(wbm[0], wbm[1]))
 if client.bet >= 128000:
    client.bet = 1000 
    return
@bot.gateway.command
def loopie(resp):
 if resp.event.ready:
  x=True
  main=time.time()
  while x:
      cf(resp)
      if time.time() - main > random.randint(1000, 2000):
        time.sleep(random.randint(500, 700))
        main=time.time()
def defination1():
  global once
  if not once:
    once=True
    if __name__ == '__main__':
      lol2= Pool(os.cpu_count() - 1)
      lol2.map(loopie)
      lol=multiprocessing.Process(target=loopie)
      lol.run()
bot.gateway.run(auto_reconnect=True)

@atexit.register
def total():
 print("{}Total Number Of Commands Executed: {}{}".format(client.color.okcyan,client.totalcmd,client.color.reset))
 print("{}Remaining Amount Of Cowoncy: {}{} {}".format(client.color.okcyan,issuechecker.cash[1],issuechecker.cash[2],client.color.reset)) 
