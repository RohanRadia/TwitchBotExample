from twitchio.ext import commands


class Moderation(commands.AutoCog):
    def __init__(self, bot):
        self.bot = bot

    def _prepare(self, bot):
        pass

    @commands.command(name='hello')
    async def _hello(self, ctx):
        await ctx.send(f'Hey there {ctx.author.name}')


def prepare(bot):
    bot.add_cog(Moderation(bot))
