import discord
import logging
from discord.client import _ColourFormatter
from discord.ext import commands
from discord.utils import get
from bot_utils import *
from calendar_utils import *
from calendar_getter import *
from time import sleep as rompiche

log = logging.getLogger("zn30")
log.setLevel(logging.DEBUG)

stream = logging.StreamHandler()
stream.setFormatter(_ColourFormatter())
log.addHandler(stream)

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

@commands.has_role(ROLES['admin'])
@bot.command()
async def clear_scheduled_events(ctx):
    guild = ctx.guild
    for scheduled_event in guild.scheduled_events:
        await scheduled_event.delete()
        rompiche(2)

@bot.command()
async def update_contest(ctx, contest):
    log.info(f"Updating contest {contest}...")
    CALENDARS[contest] = get_calendars((contest,))[contest]
    events = future_events(CALENDARS[contest])
    uids = scheduled_event_uids(ctx.guild)
    events = filter(lambda event: is_event_new(event, uids), events)
    for event in events:
        name = event.name
        log.info(f"Adding new event : {name}")
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
    log.info("Complete.")

    for emoji in bot.emojis:
        if emoji.name == contest:
            await ctx.message.add_reaction(emoji)
            return

@commands.max_concurrency(1, per=commands.BucketType.guild, wait=False)
@bot.command()
async def update(ctx):
    for contest in CONTESTS:
        await update_contest(ctx, contest)

@bot.command()
async def subscribe(ctx, contest):
    if contest not in CONTESTS:
        await ctx.reply(f"Unknown contest `{contest}`.\n"
                         "Available contests are :\n"
                         ">>>  - "+"\n - ".join(CONTESTS))
    else:
        role = ctx.guild.get_role(ROLES[contest])
        await ctx.author.add_roles(role)
        await ctx.message.add_reaction("✅")

@bot.command()
async def unsubscribe(ctx, contest):
    if contest not in CONTESTS:
        await ctx.reply(f"Unknown contest `{contest}`.\n"
                         "Available contests are :\n"
                         ">>>  - "+"\n - ".join(CONTESTS))
    else:
        role = ctx.guild.get_role(ROLES[contest])
        await ctx.author.remove_roles(role)
        await ctx.message.add_reaction("✅")

bot.run(TOKEN)
