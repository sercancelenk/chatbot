from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot("chatbot", read_only=False, logic_adapters=[
    {
        "import_path": "chatterbot.logic.BestMatch",
        "default_response": "Sorry I don't have an answer",
        "maximum_similarity_threshold": 0.9
    }
    ])

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

while True:
    user_response = input("User: ")
    print("ChatBot: ", bot.get_response(user_response))



