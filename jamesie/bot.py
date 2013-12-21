import pyrc
import pyrc.utils.hooks as hooks

class jamesie(pyrc.Bot):
    @hooks.command()
    
    def sayhi(self, channel, sender):
        self.message(channel, "Yo 'sup broz!")

if __name__ == '__main__':
    bot = jamesie("irc.freenode.net", channels = ["#jamesie"])
    bot.connect()
