import os
from discord import Intents
from discord.ext import commands
from discord.ext.commands import Context
import random
import pribeh
import cat

TOKEN = os.environ["TOKEN"]

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)


@bot.command(name="cock_rate")
async def cock_rate(ctx: Context) -> None:
    percentage = random.randint(0, 100)
    if ctx.author.id == 463805595527544832:
        await ctx.send("tvůj penis je tak otřesný že by se měl odříznout...")
    else:
        await ctx.send(
            ("rada penisu posoudila tvuj cock a dává mu finální hodnocení " +
             str(percentage) + "% solidnosti"))


@bot.command(name="story")
async def story(ctx: Context) -> None:
    await ctx.send(pribeh.story_gen())


@bot.command(name="buttping")
async def buttping(ctx: Context, num: int) -> None:
    if num in range(0, 101):
        await ctx.message.add_reaction("✅")
    else:
        await ctx.send("nemůžeš to dát přes 100%")


@bot.command(name="kočičk")
async def kocick(ctx: Context) -> None:
    await ctx.send(cat.get_random_cat())


@bot.command(name="kočičk_list")
async def kocick_list(ctx: Context) -> None:
    await ctx.send(cat.get_breed_list())


@bot.command(name="kočičk_breed")
async def kocick_breed(ctx: Context, id: str) -> None:
    await ctx.send(cat.get_specific_cat_breed(id))


#@bot.command(name="help")
#async def help(ctx: Context) -> None:
#    await ctx.send("!buttping [sila 0-100] - nepovím co to děla \n!cock_rate - ohodnoti solidnost péra\n!help - ukaže tuto spravu\n!story - vygeneruje real příběh\n!kočičk - pošle foto kočičky\n!kočičk_list - pošle list možných ras koček a jejich id\n!kočičk_breed [ID] - pošle foto specifické rasy kočky")


def run():
    assert TOKEN, "Nebyl nastaven zadny token"
    bot.run(TOKEN)
