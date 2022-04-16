from array import array
import os
import sys
import envReader
from fastapi import FastAPI
from chatterbot import ChatBot
from pydantic import BaseModel
from chatterbot.trainers import ListTrainer
bot = ChatBot(
    "YourBetterAssistant",
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    database_uri=os.environ["DB"],
    logic_adapters=[
        {"import_path": "chatterbot.logic.BestMatch"},
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I am sorry, but I do not understand.",
            "maximum_similarity_threshold": 0.90,
        },
        {
            "import_path": "chatterbot.logic.SpecificResponseAdapter",
            "input_text": "Do you have a website?",
            "output_text": "Of couse I do, here it is https://yourbetterassistant.me",
        },
        {"import_path": "chatterbot.logic.MathematicalEvaluation"},
    ],
)
args = " ".join(sys.argv)
app = FastAPI()
trainer=ListTrainer(bot)
class Body(BaseModel):
    toBeTrained:array[str]
@app.get("/")
def show_Home(message: str = "Hello"):
    return {"message": f"{bot.get_response(message)}"}

@app.post("/train")
def train_Bot(toBeTrained:Body):
    trainer.train(toBeTrained)
    return {"message":"Training"}
