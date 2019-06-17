import random

from twitchio.ext import commands

answers = ["It is certain.", "It is decidedly so.", "Without a doubt.",
           "Yes - definitely.", "Ask again later.", "Better not tell you now.",
           "Cannot predict now.", "Don't count on it."]


class Minigames(commands.AutoCog):
    def __init__(self, bot):
        self.bot = bot

    def _prepare(self, bot):
        pass

    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):
        await ctx.send(f'{ctx.author.name}, {random.choice(answers)}')


def prepare(bot):
    bot.add_cog(Minigames(bot))
