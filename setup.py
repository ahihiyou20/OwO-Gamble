import sys
import subprocess
import pkg_resources
import os
import time
required = {'discum'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if not missing:
    print("Requirement Package Are Installed Already! You're Good To Go")
    time.sleep(1)
    exit()
if missing:
    print("Installing Requirements Package...")
    time.sleep(1)
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    print("Successfully Installed Requirements Package! You're Good To Go")
    time.sleep(2)
    exit()
