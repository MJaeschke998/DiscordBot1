import discord
from discord.ext import commands
import config

#token needed for the bot to work located in the config file that is ignored by gitignore

# Intents are required for certain events such as member updates, reactions, etc.
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent if necessary
intents.members = True  # Enable the server members intent if necessary

# Create an instance of the bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Run the bot
bot.run(config.TOKEN)
