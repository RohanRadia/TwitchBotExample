import asyncio

from twitchio.ext import commands


class Help(commands.AutoCog):
    def __init__(self, bot):
        self.bot = bot

    def _prepare(self, bot):
        pass

    @commands.command(name='remind')
    async def _remind(self, ctx, mins: int = 5, *, message):
        await ctx.send(f'{ctx.author.name} You will be reminded in {str(mins)} minutes')
        await asyncio.sleep(int(mins) * 60)
        await ctx.send(f"{ctx.author.name} You told me to remind you about {message}")


def prepare(bot):
    bot.add_cog(Help(bot))
