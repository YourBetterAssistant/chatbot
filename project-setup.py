import subprocess
import subprocess
cmd=subprocess.run(["pip3", "install", "-r", "requirements.txt", ">>", "/dev/null"])
status="".join(map(chr,cmd))
print("setup.project.status.sucess")
