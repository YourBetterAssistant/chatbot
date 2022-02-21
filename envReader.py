import os
data=os.open(".env", os.O_RDONLY)
data=os.read(data, 1024)
data=data.decode("utf-8")
data=data.split("\n")

for text in data:
    os.environ[text.split("=")[0]]=text.split("=")[1]
    
