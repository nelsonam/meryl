from errbot import BotPlugin, botcmd

class HelloWorld(BotPlugin):
    @botcmd
    def hello(self, msg, args):
        return "Hello, livecoding.tv!"
