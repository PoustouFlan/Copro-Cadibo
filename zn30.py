from discord.ext import commands
import discord
from bot_utils import *
from calendar_utils import *


bot = commands.Bot(
    command_prefix = "$ ",
    help_command = None,
    intents = discord.Intents.all()
)

@bot.command()
async def week_contests(ctx, contest):
    if ctx.author.id not in ADMIN:
        await ctx.send("403 forbidden")
        return

    await ctx.message.delete()
    events = week_events(contest)
    for event in events:
        name = event.name
        begin = event.begin
        end = event.end
        description = event.description
        location = description.split('\n')[0]
        await ctx.guild.create_scheduled_event(
            name = name,
            start_time = begin,
            end_time = end,
            description = description,
            location = location,
        )

bot.run(TOKEN)
