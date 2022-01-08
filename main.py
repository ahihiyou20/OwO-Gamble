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

loop = int(input("Please Enter How Many Times It Should Loop: "))
for x in range(loop):
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
  print("[INFO] Won")
  client.sendMessage(str(channelid), "owo cash")
  minbet = 1000
  time.sleep(13)
if 'and you lost it all... :c' in msgonec:
  print("[INFO] Lost")
  client.sendMessage(str(channelid), "owo cash")
  minbet = minbet + 1000
  time.sleep(13)
if 'If you have trouble solving the captcha, please ask us in our support guild!' in msgonec:
  print("[CAPTCHA] I Found A Captcha! Come Solve It")
  exit()
if '(2/5)' in str(msgonec):
  print("CAPTCHA] I Found A Captcha! Come Solve It")
  exit()
if minbet >= maxbet:
  minbet = 100
while loop:
 main=time.time()
 if time.time() - main > random.randint(1000, 2000):
        time.sleep(random.randint(300, 600)
        main=time.time()
print(token)
client.gateway.run()
