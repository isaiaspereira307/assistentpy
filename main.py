from chatbot import Chatbot

Bot = Chatbot("Javis")

while True:
	frase = Bot.escutar()
	resp = Bot.pensar(frase)
	Bot.falar(resp)
	if resp == 'tchau':
		break