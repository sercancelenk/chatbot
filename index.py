import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

bot = ChatBot("chatbot", read_only=False, logic_adapters=[
    {
        "import_path": "chatterbot.logic.BestMatch",
        "default_response": "Sorry I don't have an answer",
        "maximum_similarity_threshold": 0.9
    }
    ])

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get")
def getChatbotResponse():
    userText = request.args.get("userMessage")
    responseJson = {};
    if userText.startswith("wheather:"):
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + userText.replace("wheather:", "") + "&appid=0ce8d887b947d503bd88c61272403a18");
        weatherResponse = response.json();
        responseJson["type"] = "weather";
        responseJson["name"] = weatherResponse["name"];
        responseJson["windspeed"] = weatherResponse["wind"]["speed"];
        responseJson["temp"] = weatherResponse["main"]["temp"];
        responseJson["feels_like"] = weatherResponse["main"]["feels_like"];
        responseJson["humidity"] = weatherResponse["main"]["humidity"];
    else:
        responseJson["type"] = "other";
        responseJson["message"] = str(bot.get_response(userText));
    return jsonify(responseJson)

if __name__ == "__main__":
    app.run(debug=True)