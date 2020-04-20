from chatbot import Chatbot
"""
import pyttsx3
import speech_recognition as sr

en = pyttsx3.init()
en.setProperty('voice',b'brazil')
rec = sr.Recognizer()

class BotFalante(Chatbot):
	def escutar(self, frase=None):
		try:
			with sr.Microphone() as mic:
				fala = rec.listen(mic)
			frase = rec.recognize_google(fala, language='pt')
			frase = frase.replace('aprendi', 'aprende')
			print(frase)
		except sr.UnknownValueError:
			print('Deu erro na identificação')
			return ''
		return super().escutar(frase=frase)

	def falar(self, frase):
		en.say(frase)
		en.runAndWait()
		super().falar(frase)

"""
Bot = Chatbot("Jarvis")
#Bot1 = BotFalante("Jarvis")

while True:
	frase = Bot.escutar()
	resp = Bot.pensar(frase)
	Bot.falar(resp)
	if resp == 'tchau':
		break