from array import array
import os
import sys
import envReader
from fastapi import FastAPI
from chatterbot import ChatBot
from pydantic import BaseModel
from chatterbot.trainers import ListTrainer
from typing import List
class TrainerBody(BaseModel):
    toBeTrained:List[str]
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
app = FastAPI()
trainer=ListTrainer(bot)
@app.get("/")
def show_Home(message: str = "Hello"):
    return {"message": f"{bot.get_response(message)}"}
@app.post("/train")
def train_Bot(body:TrainerBody):
    trainer.train(body.toBeTrained)
    return {"message":"Training"}
