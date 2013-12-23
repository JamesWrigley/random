import pyrc
import pyrc.utils.hooks as hooks

class jamesie(pyrc.Bot):
    @hooks.privmsg("^.tell\s+(?P<recipient>.+)\s+(?P<msg>.+)$")
    def tell(self, target, sender, **kwargs):
        user_messages = {}

        self.message(target, "{0}: Ok, I'll tell {1} that next time I see them.".format(sender, kwargs["recipient"]))
        user_messages[kwargs["recipient"]] = kwargs["msg"]
        self.message(target, "{0}: {1} says \"{2}\"".format(kwargs["recipient"], sender, user_messages[kwargs["recipient"]]))

    @hooks.privmsg("^.repeat\s+(?P<msg>.+)$")
    def repeat(self, target, sender, **kwargs):
        if target.startswith("#"):
            self.message(target, kwargs["msg"])
        else:
            self.message(sender, kwargs["msg"])

    @hooks.privmsg("(.fail|.lamb|.help)")
    def runCommand(self, target, sender, *args):
        commands = [".tell", ".fail", ".repeat", ".lamb", ".help"]

        if target.startswith("#"):
            if args[0] == ".fail":
                self.message(target, "Abject, miserable, despondent, failure.")
            elif args[0] == ".lamb":
                self.message(target, "LAAAYUUMBB")
            elif args[0] == ".help":
                self.message(target, "{0}: I am a weird chap. Current commands are {1}.".format(sender, ", ".join(commands)))
            else:
                self.message(target, "Unrecognised command")


if __name__ == '__main__':
    bot = jamesie("irc.freenode.net", channels = ["#jamesie"])
    bot.connect()
