from discord.ext import commands
from discord import ScheduledEvent
from bot_utils import *
from calendar_utils import *


bot = commands.Bot(command_prefix = "$ ", help_command = None)

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
        channel = bot.get_channel(CHANNELS[contest])
        await create_scheduled_event(
            name = name,
            start_time = begin,
            end_time = end,
            channel = channel,
            description = description
        )

bot.run(TOKEN)
