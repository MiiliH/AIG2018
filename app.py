from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
import sys
import traceback
import logging
import googleSearch as gs
import Chatbot.chat as chat
import translate as tr
from Translate import EncoderRNN
from Translate import AttnDecoderRNN

state = {
    'debug': False,
    'translate': False,
    'search': False
}

input_style = Style.from_dict({
    '': '#33aa33 bold',
})

def exit():
    print("See you later alligator!")
    sys.exit()

def getTranslation(user_input, state):
    try:
        translate = tr.translate(user_input);
    except KeyError:
        if state['debug']:
            logging.error(traceback.format_exc())
        else:
            translate = "Ouh, man. I don't know that word"
    return translate
def getSearch(user_input, state):
	search = gs.search(user_input);
	return search
def getOutput(user_input, state):
    if user_input == "debug":
        state['debug'] = True
        return "I let you know what is inside me"
    if user_input == "stop debug":
        state['debug'] = False
        return "I will keep my poker face from now on"
    if user_input == "exit" or user_input == "quit" or user_input == "bye" or user_input == "Bye" or user_input == "goodbye" or user_input == "Goodbye" or user_input == "Exit" or user_input == "Quit":
       print(user_input)
       exit()
    if user_input == "please translate" or user_input == "Please translate" or user_input == "Translate" or user_input == "translate":
        state['translate'] = True
        return "Sure, I will translate from Oshiwambo to English"
    if user_input == "stop translating":
        state['translate'] = False
        return "Okay, let's talk about something"
    if user_input == "please search" or user_input == "Please search" or user_input == "search" or user_input == "Search":
	    state['search']  = True
	    return "What do you want to search about"
    if user_input == "stop searching":
	    state['search'] = False
	    return "Okay, is there anything else"

    if state['search']:
	    return getSearch(user_input, state)
    if state['translate']:
        return getTranslation(user_input, state)
    else:
        return chat.respond(user_input)


if __name__ == '__main__':
    while True:
        try:
            answer = prompt('You: ', style=input_style)
            print('Bot: %s' % getOutput(answer, state))
        except EOFError:
            pass
        except KeyboardInterrupt:
            exit()
        except Exception: # catch *all* exceptions
            if state['debug']:
                logging.error(traceback.format_exc())
