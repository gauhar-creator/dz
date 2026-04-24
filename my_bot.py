import telebot
from google import genai

# Твой токен от @BotFather
TELEGRAM_TOKEN = "8524346926:AAEv7He34qdceg3jMIM3xmeLl5TJHXdDN30"


GEMINI_API_KEY = "AIzaSyCDO614_0A8i6L0X5Yolgxk3XlCHKcNwy8" 

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Бот готов к работе! Спрашивай что угодно.")

@bot.message_handler(content_types=['text'])
def ai_reply(message):
    try:
        
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=message.text
        )
        bot.send_message(message.chat.id, response.text)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

print("Бот запущен и ждет сообщений...")
bot.infinity_polling()