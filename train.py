from os import environ
import os
import envReader
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
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
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("./messages/")
trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.trivia", "chatterbot.corpus.english.psychology", "chatterbot.corpus.english.humor")

trainer=ListTrainer(bot)
trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you.",
    "You are welcome."
])
trainer.train([
    "What is your name?",
    "My name is YourBetterAssistant.",
    "That is a nice name.",
    "Thank You!",
    "You are welcome."
    "I am glad to meet you."
])
trainer.train([
    "What is your favorite color?",
    "My favorite color is Green.",
    "That is a nice color.",
    "Thank You!",
    "You are welcome."
])
print("Done Importing")
while True:
    try:
        bot_input = bot.get_response(input())
        print(f"{bot_input}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break

