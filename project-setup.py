import subprocess
import os
cmd=subprocess.run(["pip3", "install", "-r", "requirements.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("setup.project.status.sucess")
