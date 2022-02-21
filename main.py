import os
import sys
import envReader
from fastapi import FastAPI
from chatterbot import ChatBot
bot = ChatBot('YourBetterAssistant', 
        storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
        database_uri=os.environ["DB"],
)
args=" ".join(sys.argv)
app = FastAPI()

@app.get("/")
def show_Home(message: str = "Hello"):
        return {"message": f"{bot.get_response(message)}"}