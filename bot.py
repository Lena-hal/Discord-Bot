import os
import socket
import discord
from discord import Intents
from discord import app_commands
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
import threading


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

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "kocick", description = "pošle obrázek kočičky") 
@app_commands.guilds(*command_settings.kocick)
async def kocick(ctx):
    await ctx.response.send_message(cat.get_random_cat())



@tree.command(name = "cockrate", description = "zhodnotí solidnost tvého péra") 
@app_commands.guilds(*command_settings.cockrate)
async def cock(ctx):
    percentage = random.randint(0, 100)
    if ctx.user.id == 463805595527544832:
        await ctx.response.send_message("tvůj penis je tak otřesný že by se měl odříznout...")
    else:
        await ctx.response.send_message(
            ("rada penisu posoudila tvuj cock a dává mu finální hodnocení " +
            str(percentage) + "% solidnosti"))
        

@tree.command(name = "story", description = "pošle epický příběh!") 
@app_commands.guilds(*command_settings.story)
async def story(ctx):
    if ctx.guild.id in command_settings.story:
        await ctx.response.send_message(pribeh.story_gen())
    else:
        return
        
@tree.command(name = "fem_meme", description="pošle nějaký epický feminní meme")
@app_commands.guilds(*command_settings.fem_meme)
async def get_random_meme(ctx):
    subreddit_list=["egg_irl", "traaaaaaannnnnnnnnns", "4tran",
                    "femboymemes"]
    reddit = asyncpraw.Reddit(client_id=reddit_client_id,
                                  user_agent="okkr_bot:v0.0.1",
                                  client_secret=reddit_client_secret)
    subreddit_name = random.choice(subreddit_list)
    subreddit = await reddit.subreddit(subreddit_name)
    hot_posts = subreddit.hot(limit=100)
    memes = []
    async for post in hot_posts:
        memes.append(post)

    await ctx.response.send_message(random.choice(memes).url)
    await reddit.close()


@client.event
async def on_message(message):
    if message.author.id == 1051272546391167056:  #okkr bot
        return
    if message.author.id == 353932703483166723:  # starmex jdu kadit
        if "kadit" in message.content.lower() or "kakat" in message.content.lower():
            await message.add_reaction(EMOJI_POO)
    
    for word in ["srst","fur"]:
        if word in message.content.lower():
            number = message.content.lower().count(word)
            for _ in range(number):
                await message.reply("Vojtivák")
    for word in ["loli","dítě"]:
        if word in message.content.lower():
            number = message.content.lower().count(word)
            for _ in range(number):
                await message.reply("Lena")
    
    if message.content.lower() == "!nerdify":
        nerd = message.reference.cached_message.content
        state = False

        result = ""

        for i in nerd:
            if state == False:
                state = True
                result += i.lower()
            else:
                state = False
                result += i.capitalize()
            if i == " ":
                result += ":nerd: "

        if len(result) > 2000:
            await message.delete()
        else:
            await message.reference.cached_message.reply(result)
            await message.delete()
        

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
                        content="účet neexistuje (kód od Lenči :3)")
        except Exception as e:
            await message.reply(
                content=
                "nepodařilo se ověřit reddit účet zkus to znova asi idk (kód od Lenušky)"
            )

@client.event
@app_commands.guilds(*command_settings.all)
async def on_ready():
    for i in command_settings.all:
        print(await tree.sync(guild=discord.Object(id=i)))
    
    print("Ready!")


def run():
    assert TOKEN, "Nebyl nastaven zadny token"
    client.run(TOKEN)
