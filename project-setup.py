import subprocess
cmd=subprocess.run(["pip3", "install", "-r", "requirements.txt"])
status="".join(map(chr,cmd))
print(status)
