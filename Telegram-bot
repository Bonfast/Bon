import telebot
import requests
import json

TOKEN = '6060126631:AAEt6OVcpnOQMxa42olebhPFbUwCC-46bjA'

bot = telebot.TeleBot(TOKEN)


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: float) -> float:
        base = base.upper()
        quote = quote.upper()
        url = f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}"
        response = requests.get(url)
        data = json.loads(response.text)

        if response.status_code != 200:
            raise APIException(f"Ошибка при получении курса валюты: {data['Message']}")

        if quote not in data:
            raise APIException(f"Невозможно конвертировать валюту '{base}' в '{quote}'")

        price = data[quote]
        result = price * amount
        return result


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    instructions = (
        "Привет! Я бот для конвертации валют.\n\n"
        "Чтобы узнать стоимость валюты, отправьте сообщение в следующем формате:\n"
        "<валюта для конвертации> <валюта, в которую нужно перевести> <количество первой валюты>\n\n"
        "Например, для конвертации 10 евро в доллары:\n"
        "евро доллар 10(на английском языке из вкладки value)\n\n"
        "Доступные команды:\n"
        "/start - Начать использование бота и получить инструкции\n"
        "/help - Получить инструкции\n"
        "/values - Получить список всех доступных валют"
    )
    bot.reply_to(message, instructions)


@bot.message_handler(commands=['values'])
def handle_values(message):
    currencies = (
        "Доступные валюты:\n"
        "евро (EUR)\n"
        "доллар (USD)\n"
        "рубль (RUB)"
    )
    bot.reply_to(message, currencies)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        text = message.text.upper().split()
        if len(text) != 3:
            raise ValueError

        currency, quote, amount = text
        converted_amount = CurrencyConverter.get_price(currency, quote, float(amount))
        response = f"{amount} {currency} = {converted_amount} {quote}"
    except ValueError:
        response = "Неверный формат ввода. Пожалуйста, используйте следующий формат:\n" \
                   "<валюта для конвертации> <валюта, в которую нужно перевести> <количество первой валюты>"
    except APIException as e:
        response = f"Ошибка API: {e}"

    bot.reply_to(message, response)


if __name__ == "__main__":
    bot.polling()
