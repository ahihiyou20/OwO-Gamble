#Import important package

import os
import time
import random
try:
import discum
except:
 if os.name == 'nt':
os.system('py -m pip install discum')
if os.name != 'nt':
print('You Should Install Package "Discum"')
import discum

#Var
token = input('Please Enter Your Account Token: ')
channelid = input('Please Enter Your Channel ID: ')
owoid = str(408785106942164992)
minbet = 1000
maxbet = input('Please Enter Maximum Bet: ')

#Main Code

client=discum.Client(token=token, log=False)

def runner()
cfmin = owo coinflip {minbet}
msgs=client.getMessages(str(bot.channel),num=10)
   msgs=json.loads(msgs.text)
   owodes=0 
   for msgone in msgs:
    if msgone['author']['id']==str(owoid):
      owodes=owodes+1
      msgonec=msgone['content']
client.typingAction(str(channelid))
client.sendMessage(str(channelid), cfmin)
print("[SENT] {cfmin}")
if 'and you won' in msgonec:
  print("[WIN] Win
if 'and you lost it all... :c' in msgonec:
  minbet = minbet 
if minbet >= maxbet:
  minbet = 1000
