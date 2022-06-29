from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("chatbot", read_only=False, logic_adapters=[
    {
        "import_path": "chatterbot.logic.BestMatch",
        "default_response": "Sorry I don't have an answer",
        "maximum_similarity_threshold": 0.9
    }
    ])

list_to_train = [
    "hi",
    "hi there",
    "how are you?",
    "I'm always fine :)",
    "what's your name",
    "I'm a chatbot",
    "how old are you?",
    "I'm ageless!!",
    "Why are you so mad?",
    "I'm not!",
    "Do you have Iphone?",
    "I have everything",
    "What's your favourite food?",
    "I don't eat anything",
    "I'm here to answer your questions.",
    "I don't know what you're talking about"
]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)

while True:
    user_response = input("User: ")
    print("ChatBot: ", bot.get_response(user_response))



