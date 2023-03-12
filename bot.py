import os
import socket
from discord import Intents
from discord.ext import commands
from discord.ext.commands import Context
import random
import pribeh
import cat
import okkr_verify
import random
import asyncpraw
import asyncio
from dotenv import load_dotenv
import database_controller as dbc
import command_settings


"""
TODO: 
analizace četnosti slov a nasledna soutěž o "slovo dne" z vyběru top 1000 slov
přikaz na každou osobu ktera vygeneruje random větu z chat logu té osoby
list vtipnych slov ktere by udělali odpověď
když někdo napiše levlí tak to odpoví random hlaškou
"""


EMOJI_POO = "💩"

if socket.gethostname() == "DESKTOP-S0FLL2V":
    load_dotenv("udaje.env")
    TOKEN = os.getenv("TOKEN")
    reddit_client_id = os.getenv("client_id")
    reddit_client_secret = os.getenv("client_secret")
else:
    TOKEN = os.environ["TOKEN"]
    reddit_client_id = os.environ["client_id"]
    reddit_client_secret = os.environ["client_secret"]

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",
                   case_insensitive=True,
                   intents=intents,
                   help_command=None)


@bot.event
async def on_message(message):
    if message.author.id == 1051272546391167056:  #okkr bot
        return
    if message.author.id == 353932703483166723:  # starmex jdu kadit
        if "kadit" in message.content or "kakat" in message.content:
            await message.add_reaction(EMOJI_POO)

    if message.channel.id == 1061712331949735976:
        try:
            if not (" " in message.content):
                auth = await okkr_verify.auth_user(message.content)
                if auth == True:
                    await message.reply(content="odteď není cesty zpět :)")
                    await message.author.add_roles(
                        message.guild.get_role(1061710908637851668))
                else:
                    await message.reply(
                        content="účet neexistuje (kód od Lenušky)")
        except Exception as e:
            print(e)
            await message.reply(
                content=
                "nepodařilo se ověřit reddit účet zkus to znova asi idk (kód od Lenušky)"
            )

    await bot.process_commands(message)


@bot.command(name="cock_rate")
async def cock_rate(ctx: Context) -> None:
    if ctx.guild.id in command_settings.cockrate:
        percentage = random.randint(0, 100)
        if ctx.author.id == 463805595527544832:
            await ctx.send("tvůj penis je tak otřesný že by se měl odříznout...")
        else:
            await ctx.send(
                ("rada penisu posoudila tvuj cock a dává mu finální hodnocení " +
                str(percentage) + "% solidnosti"))


@bot.command(name="story")
async def story(ctx: Context) -> None:
    if ctx.guild.id in command_settings.story:
        await ctx.send(pribeh.story_gen())
    else:
        return


@bot.command(name="buttping")
async def buttping(ctx: Context, num: int) -> None:
    if ctx.guild.id in command_settings.buttping:
        if num in range(0, 101):
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("nemůžeš to dát přes 100%")
    else:
        return


@bot.command(name="kočičk")
async def kocick(ctx: Context) -> None:
    if ctx.guild.id in command_settings.kocick:
        await ctx.send(cat.get_random_cat())


@bot.command(name="kočičk_list")
async def kocick_list(ctx: Context) -> None:
    if ctx.guild.id in command_settings.kocick:
        await ctx.send(cat.get_breed_list())


@bot.command(name="kočičk_breed")
async def kocick_breed(ctx: Context, id: str) -> None:
    if ctx.guild.id in command_settings.kocick:
        await ctx.send(cat.get_specific_cat_breed(id))


@bot.command(name="help")
async def help(ctx: Context) -> None:
    ctx.send("Toto je pořad ještě ve vívoji, zatím tu nic není")

@bot.command(name="fem_meme")
async def get_random_meme(
    ctx: Context,
    subreddit_list=["egg_irl", "traaaaaaannnnnnnnnns", "4tran",
                    "femboymemes"]):
    if ctx.guild.id in command_settings.kocick:
        reddit = asyncpraw.Reddit(client_id=reddit_client_id,
                                  user_agent="okkr_bot:v0.0.1",
                                  client_secret=reddit_client_secret)
        subreddit_name = random.choice(subreddit_list)
        subreddit = await reddit.subreddit(subreddit_name)
        hot_posts = subreddit.hot(limit=100)
        memes = []
        async for post in hot_posts:
            memes.append(post)

        await ctx.send(random.choice(memes).url)
        await reddit.close()


def run():
    assert TOKEN, "Nebyl nastaven zadny token"
    bot.run(TOKEN)
