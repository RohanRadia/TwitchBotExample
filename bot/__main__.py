import json
from os import environ

from twitchio.ext import commands

initial_extensions = ['cogs.moderation', 'cogs.minigames', 'cogs.help']

with open("settings.json", "r") as f:
    settings = json.load(f)


class Bot(commands.Bot):
    def __init__(self, irc_token, nick, client_id='test', initial_channels=['MutantReaperBot',]):
        params = {
            'irc_token': irc_token,
            'client_id': client_id,
            'nick': nick,
            'prefix': '!',
            'initial_channels': initial_channels,
        }
        super().__init__(**params)

        for extension in initial_extensions:
            try:
                self.load_module(extension)
                print(f"Successfully loaded {extension}")
            except Exception as e:
                print(f'Failed to load extension {extension}.')
                print(e)

    async def event_ready(self):
        print(f"Ready: {self.nick}")

    async def event_message(self, message):
        await self.handle_commands(message)


if __name__ == '__main__':
    channels = ['MutantReaperBot',]
    bot = Bot(irc_token=settings["IRC_TOKEN"], client_id=settings["CLIENT_ID"], nick=settings["NICK"],
              initial_channels=channels)
    bot.run()
