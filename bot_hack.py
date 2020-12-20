import telebot
import config_bot


bot = telebot.TeleBot(config_bot.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Вітаю, цей бот було створено командою "Teаm of Legends", він допоможе вам знайти хорші місця у місті Львів')


@bot.message_handler(commands=['hist'])
def hist(message):
	bot.send_message(message.chat.id, 'Ось мої улюблені пам\'ятки Львова')
	bot.send_photo(message.chat.id, open('photos/rynok.jpg', 'rb'), caption=config_bot.runokt)
	bot.send_photo(message.chat.id, open('photos/zamok.jpg', 'rb'), caption=config_bot.zamokt)
	bot.send_photo(message.chat.id, open('photos/opera.jpg', 'rb'), caption=config_bot.operat)
	bot.send_photo(message.chat.id, open('photos/palace.jpg', 'rb'), caption=config_bot.palacet)
	bot.send_photo(message.chat.id, open('photos/latct.jpg', 'rb'), caption=config_bot.lactt)


@bot.message_handler(commands=['chill'])
def chill(message):
	bot.send_message(message.chat.id, 'Залітай, тут завжди жарко')
	bot.send_photo(message.chat.id, open('photos/rent.jpg', 'rb'), caption=config_bot.rentt)
	bot.send_photo(message.chat.id, open('photos/fclub.jpg', 'rb'), caption=config_bot.fclubt)
	bot.send_photo(message.chat.id, open('photos/hlb.jpg', 'rb'), caption=config_bot.hlbt)
	bot.send_photo(message.chat.id, open('photos/picasso.jpg', 'rb'), caption=config_bot.picassot)
	bot.send_photo(message.chat.id, open('photos/rinf.jpg', 'rb'), caption=config_bot.rinft)


@bot.message_handler(commands=['alone'])
def alone(message):
	bot.send_message(message.chat.id, f'Уже відвідав місця з нашої підбірки?\nНе маєш з ким обговорити чи піти?\nШвиденько залітай сюди і ділися своїми враженнями:\n{config_bot.chat}')


@bot.message_handler(commands=['love'])
def love(message):
	bot.send_message(message.chat.id, 'Ось найкращі та найгарніші місця у Львові щоб провести час зі своєю другою половинкою')
	bot.send_photo(message.chat.id, open('photos/striyskiy-park.jpg', 'rb'), caption=config_bot.striyskiy)
	bot.send_photo(message.chat.id, open('photos/lesia.jpg', 'rb'), caption=config_bot.lesia)
	bot.send_photo(message.chat.id, open('photos/kiss.jpg', 'rb'), caption=config_bot.kiss)
	bot.send_photo(message.chat.id, open('photos/vulitsya.jpg', 'rb'), caption=config_bot.vul)
	bot.send_photo(message.chat.id, open('photos/franko.jpg', 'rb'), caption=config_bot.franko)


@bot.message_handler(commands=['tour'])
def tour(message):
	with open('tour.txt', 'r') as t:
		bot.send_message(message.chat.id, t.read())


@bot.message_handler(content_types=['text'])
def reply(message):
	bot.send_message(message.chat.id, message.text)
	bot.send_message(message.chat.id, f'Як бачиш з мене співрозмовник поганий.\nЗаходи у цей чат, знайомся, спілкуйся\nСкажу по секрету тут зібралися найкращі люди, яких я коли-небудь знав\n{config_bot.chat}')


if __name__ == '__main__':
    bot.polling(none_stop=True)