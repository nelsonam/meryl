from errbot import BotPlugin, botcmd

class HelloWorld(BotPlugin):
    @botcmd
    def hello(self, msg, args):
        return "Hello, livecoding.tv!"

    @botcmd
    def goodbye(self, msg, args):
        return "Goodbye, cruel world!"

    @botcmd
    def bot(self, msg, arg):
        return "Hello, I am Meryl. I was created by allisonanalytics and singlerider."
