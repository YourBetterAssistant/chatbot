from os import environ
import os
import envReader
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
basicWords=[
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you.",
    "You are welcome.",
]
bot = ChatBot('YourBetterAssistant', 
        storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
        database_uri=os.environ["DB"],
)
ListTrainer(bot).train(basicWords)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)
red="\u001b[31m"
while True:
    try:
        bot_input = bot.get_response(input())
        print(f"{red} {bot_input}")

    except(KeyboardInterrupt, EOFError, SystemExit):
        break