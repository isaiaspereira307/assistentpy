from chatbot import Chatbot

Bot = Chatbot("Felipe")

while True:
	frase = Bot.escutar()
	resp = Bot.pensar(frase)
	Bot.falar(resp)
	if resp == 'tchau':
		break