import os
import discord
from discord import Intents, Message
from discord.ext import commands
from discord.ext.commands import Context
from discord.utils import get
from dotenv import load_dotenv
import random
import pribeh

load_dotenv("udaje.env")
TOKEN = os.getenv('DISCORD_TOKEN')

print(TOKEN)

intents = Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(
    command_prefix="!", case_insensitive=True, intents=intents
)

@bot.command(name="cock_rate")
async def cock_rate(ctx: Context) -> None:
    percentage = random.randint(0,100)
    if ctx.author.id == 463805595527544832:
        await ctx.send("tvůj penis je tak otřesný že by se měl odříznout...")    
    else:
        await ctx.send(("rada penisu posoudila tvuj cock a dává mu finální hodnocení " + str(percentage) + "% solidnosti"))

@bot.command(name="story")
async def story(ctx: Context) -> None:
    await ctx.send(pribeh.story_gen())

@bot.command(name="buttping")
async def buttping(ctx: Context, num: int) -> None:
    if num in range(0, 101):
        await ctx.message.add_reaction("✅")
    else:
        await ctx.send("nemůžeš to dát přes 100%")

@bot.event
async def on_raw_reaction_add(payload):
    reaction = payload.emoji
    user = payload.member
    if payload.channel_id != 1051585791782043698:
        return
    if reaction.name == "1️⃣":
        Role = get(user.guild.roles, name="she/her")
    if reaction.name == "2️⃣":
        Role = get(user.guild.roles, name="he/him")
    if reaction.name == "3️⃣":
        Role = get(user.guild.roles, name="they/them")

    await user.add_roles(Role)

@bot.event
async def on_raw_reaction_remove(payload):
    reaction = payload.emoji
    user = payload.member
    if payload.channel_id != 1051585791782043698:
        return
    if reaction.name == "1️⃣":
        Role = get(user.guild.roles, name="she/her")
    if reaction.name == "2️⃣":
        Role = get(user.guild.roles, name="he/him")
    if reaction.name == "3️⃣":
        Role = get(user.guild.roles, name="they/them")

    await user.remove_roles(Role)

assert TOKEN, "Nebyl nastaven zadny token"
bot.run(TOKEN)

os.getenv("TOKEN")