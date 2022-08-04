from discord.ext import commands
import discord
from bot_utils import *
from calendar_utils import *


bot = commands.Bot(
    command_prefix = "$ ",
    help_command = None,
    intents = discord.Intents.all()
)

@admin_only
@bot.command()
async def clear_scheduled_events(ctx):
    guild = ctx.guild
    for scheduled_event in guild.scheduled_events:
        await scheduled_event.delete()

@admin_only
@bot.command()
async def future_contests(ctx, contest):
    await ctx.message.delete()
    events = future_events(contest)
    for event in events:
        name = event.name
        begin = event.begin
        end = event.end
        description = f"{event.description}\nuid: {event.uid}"
        location = description.split('\n')[0].split('Link: ')[1]
        await ctx.guild.create_scheduled_event(
            name = f"{DISPLAY[contest]} {name}",
            start_time = begin,
            end_time = end,
            description = description,
            location = location,
        )

bot.run(TOKEN)
