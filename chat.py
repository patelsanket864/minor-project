import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/dell/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
	data = open('C:/Users/dell/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files , 'r').readlines()
	bot.train(data)

while True:
	message=input('you:' )
	if message.strip() !='Bye' :
		reply=bot.get.response(message)
		print('chatbot : ',reply)
		print('chatbot',reply)
	if message.strip() =='Bye' :
		print('chatbot : bye')
		break