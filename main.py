import json
import telebot
import requests


bot = telebot.TeleBot('6813458455:AAGXnfRjt9QfMTplK5RrierayhzRCaxL1m4')
api = 'e6e7347b0b7c998aa4474e708f787ea0'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, what's up? Write a name of the city")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    respond = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if respond.status_code == 200:
        data = json.loads(respond.text)
        temp = data['main']['temp']
        bot.reply_to(message, f"The weather in {data['name']} is {temp}°C")


        image = 'warm.png' if int(temp) >= 10.0 else 'cold.jpg'
        file = open(image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Ooops, I couldn't find this city")


bot.polling(non_stop=True)