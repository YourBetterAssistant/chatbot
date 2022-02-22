from os import environ
import os
import envReader
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

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
trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")
while True:
    try:
        bot_input = bot.get_response(input())
        print(f"{bot_input}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
