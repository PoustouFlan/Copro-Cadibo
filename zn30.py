from discord.ext import commands
from bot_utils import *
from calendar_utils import *


bot = commands.Bot(command_prefix = "$ ", help_command = None)

@bot.command()
async def week_contests(ctx, contest):
    await ctx.message.delete()
    events = week_events(contest)
    for event in events:
        await ctx.send(event_message(event, contest))

bot.run(TOKEN)
