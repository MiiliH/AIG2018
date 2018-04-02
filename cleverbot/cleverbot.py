import requests

class cleverBot:
    """ A simple wrapper class for the www.cleverbot.com api. """

    url = "https://www.cleverbot.com/getreply"
    
    def __init__(self, api_key, name="CleverBot"):
        """ Initialize the class with an api key and optional name 
        :type name: string
        :type api_key: string
        :type history: dict or maybe a list
        :type convo_id: string
        :type cs: string
        :type count: int
        :type time_elapsed: int
        :type time_taken: int
        :type output: string
        """
        self.name = name
        self.key = api_key
        self.history = {}
        self.convo_id = ""
        self.cs = ""
        self.count = 0
        self.time_elapsed = 0
        self.time_taken = 0
        self.output = ""

    def say(self, text):
        """ 
        Say something to www.cleverbot.com
        :type text: string
        Returns: string
        """

        params = {
            "input": text,
            "key": self.key,
            "cs": self.cs,
            "conversation_id": self.convo_id,
            "wrapper": "CleverWrap.py"
        }

        reply = self._send(params)
        self._process_reply(reply)
        return self.output


    def _send(self, params):
        """
        Make the request to www.cleverbot.com
        :type params: dict
        Returns: dict
        """
        # Get a response
        try:
            r = requests.get(self.url, params=params)
        # catch errors, print then exit.
        except requests.exceptions.RequestException as e:
            print(e)
        return r.json(strict=False)  # Ignore possible control codes in returned data


    def _process_reply(self, reply):
        """ take the cleverbot.com response and populate properties. """
        self.cs = reply.get("cs", None)
        self.count = int(reply.get("interaction_count", None))
        self.output = reply.get("output", None)
        self.convo_id = reply.get("conversation_id", None)
        self.history = {key:value for key, value in reply.items() if key.startswith("interaction")}
        self.time_taken = int(reply.get("time_taken", None))
        self.time_elapsed = int(reply.get("time_elapsed", None))

    def reset(self):
        """
        Drop values for self.cs and self.conversation_id
        this will start a new conversation with the bot.
        """
        self.cs = ""
        self.convo_id = ""
