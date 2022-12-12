import os
import discord
from discord import Intents, Message
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv
import random
import pribeh

TOKEN = os.environ["TOKEN"]

intents = Intents.default()
intents.message_content = True

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

assert TOKEN, "Nebyl nastaven zadny token"
bot.run(TOKEN)

os.getenv("TOKEN")
