from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
import sys
import traceback
import logging

import Chatbot.chat as chat
import translate as tr
from Translate import EncoderRNN
from Translate import AttnDecoderRNN

state = {
    'debug': False,
    'translate': False
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

def getOutput(user_input, state):
    if user_input == "debug":
        state['debug'] = True
        return "I let you know what is inside me"
    if user_input == "stop debug":
        state['debug'] = False
        return "I will keep my poker face from now on"
    if user_input == "exit" or user_input == "quit" or user_input == "bye":
       print(user_input)
       exit()

    if user_input == "please translate":
        state['translate'] = True
        return "Sure, I will translate from Oshiwambo to English"
    if user_input == "stop translating":
        state['translate'] = False
        return "Okay, let's talk about something"

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
