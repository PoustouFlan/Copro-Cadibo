import discord
from discord.ext import commands
from bot_utils import *
from calendar_utils import *
from calendar_getter import *
from time import sleep as rompiche

CALENDARS = {}

bot = commands.Bot(
    command_prefix = "$ ",
    help_command = None,
    intents = discord.Intents.all()
)

def scheduled_event_uids(guild):
    uids = set()
    for scheduled_event in guild.scheduled_events:
        description = scheduled_event.description
        uid = description.split("\nuid: ")[1]
        uids.add(uid)
    return uids

def is_event_new(event, uids):
    return event.uid not in uids

@admin_only
@bot.command()
async def clear_scheduled_events(ctx):
    guild = ctx.guild
    for scheduled_event in guild.scheduled_events:
        await scheduled_event.delete()
        rompiche(2)

@bot.command()
async def update_contest(ctx, contest):
    debug(f"Updating contest {contest}...")
    CALENDARS[contest] = get_calendars((contest,))[contest]
    events = future_events(CALENDARS[contest])
    uids = scheduled_event_uids(ctx.guild)
    events = filter(lambda event: is_event_new(event, uids), events)
    for event in events:
        name = event.name
        debug(f"Adding new event : {name}")
        begin = event.begin
        end = event.end
        description = f"{event.description}uid: {event.uid}\n"
        location = description.split('\n')[0].split('Link: ')[1]
        icon = contest_icon(contest)

        if icon is not None:
            await ctx.guild.create_scheduled_event(
                name = f"{DISPLAY[contest]} {name}",
                start_time = begin,
                end_time = end,
                description = description,
                location = location,
                image = icon,
            )
        else:
            await ctx.guild.create_scheduled_event(
                name = f"{DISPLAY[contest]} {name}",
                start_time = begin,
                end_time = end,
                description = description,
                location = location,
            )
        rompiche(4)
    debug("Complete.")

@commands.max_concurrency(1, per=commands.BucketType.guild, wait=False)
@bot.command()
async def update(ctx):
    for contest in CONTESTS:
        await update_contest(ctx, contest)

bot.run(TOKEN)
