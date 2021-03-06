"""This file will launch the bot and load all cogs."""

import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
djtbot = commands.Bot(command_prefix='$', intents=intents)

@djtbot.check
def check_guild(ctx):
    try:
        return ctx.guild.id == 948016353263124521 # Current guild id
    except AttributeError:
        return True

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        djtbot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded the following cog: {filename}")

# djtbot.load_extension(f'cogs.emoji_manager')

with open("token_new.txt") as token_file:
    bot_token = token_file.read()

djtbot.run(bot_token)


