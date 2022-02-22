import os
import sys
import envReader
from fastapi import FastAPI
from chatterbot import ChatBot

print("hello")
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
        {"import_path": "chatterbot.logic.TimeLogicAdapter"},
    ],
)
args = " ".join(sys.argv)
app = FastAPI()


@app.get("/")
def show_Home(message: str = "Hello"):
    return {"message": f"{bot.get_response(message)}"}
