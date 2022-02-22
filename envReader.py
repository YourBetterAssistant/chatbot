import os

data = os.open(".env", os.O_RDONLY)
data = os.read(data, 1024)
data = data.decode("utf-8")
data = data.split("\n")

for text in data:
    text = text.split("=")
    if len(text) < 1:
        break
    os.environ[text[0]] = text[1]
