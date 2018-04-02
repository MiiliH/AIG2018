from cleverbot.cleverbot import cleverBot

api_key= cleverBot("CC8h4QuulAoL42JxZP6Afc_Lkzw")

#while i am still connected keep the conversation going.
def main():
    while True:
        user_input = input("You :")
        output = api_key.say(user_input)
        print("Bot :" + output)
        if user_input == "bye" or user_input == "Bye" or user_input == "Good day" or user_input == "good day" or user_input == "see you":
	        break
    print("Bot :It was a pleasure to chat with. Bye")

#in case of error  
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('>> Exiting...')
    except Exception as err:
        print("Connection problem, Ensure you have internet connection.")
