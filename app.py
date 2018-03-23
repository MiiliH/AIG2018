from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
import Translate as tr
from Translate import EncoderRNN
from Translate import AttnDecoderRNN
import sys
import traceback
import logging

state = {
    'debug': False
}

input_style = Style.from_dict({
    '': '#33aa33 bold',
})

def exit():
    print("See you later alligator!")
    sys.exit()

def getOutput(user_input, state):
    if user_input == "debug":
        state['debug'] = True
        return "I let you know what is inside me"
    if user_input == "stop debug":
        state['debug'] = False
        return "I will keep my poker face from now on"
    if user_input == "exit" or user_input == "quit" or "bye":
        exit()
    try:
        translate = tr.translate(user_input);
    except KeyError:
        if state['debug']:
            logging.error(traceback.format_exc())
        else:
            translate = "Ouh, man. I don't know that word"
    return translate


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
