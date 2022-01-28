import time
import json
import os
if os.name == 'nt':
    pass
if os.name == 'linux':
    import simplejson as json
else:
    try:
        import json
    except:
        import simplejson as json
file = open("settings.json", "r")
data = json.load(file)
file.close()
data['token'] = input("Please Enter Your Account Token: ")
data['channel'] = input("Please Enter Your Channel ID: ")
file = open("settings.json", "w")
json.dump(data, file)
file.close()
print('Successfully saved!')
print('Please Restart The Command Prompt')
time.sleep(2)
exit()

