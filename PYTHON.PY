# run these commands on your terminal 
pip install chatterbot
pip install chatterbot_corpus

# open a 'chatbot.py' and write these codes inside it

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='MeroBot', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

from chatterbot.trainers import ChatterBotCorpusTrainer

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')


print("Bot: Ask me anything.")

exit_list = ['close', 'exit', 'bye', 'quit', 'stop']

while True:
    user_input = input()
    if user_input.lower() in exit_list:
        print("Hope you liked by service")
        break
    else:
        print(my_bot.get_response(user_input))
