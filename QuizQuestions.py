import discord
from discord.ext import commands
import random
import os

description = """Hey! I'm your learning assistant for Computational Intelligence
            and Machine Learning I. I will ask you different questions regarding
             the topics in the course, and you can discuss the answers. I will
             not check your answers though, the Admins may do that ;)"""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("-------------------------------------------")

@bot.command()
async def question(ctx):
    """
    Posts a random question of the quiz questions channel into the current
    channel.
    Type :question
    """
    #print("Question")
    #channel = bot.get_channel(1073229394501447690) # Testchannel on my testserver
    channel = bot.get_channel(1072079980235857951) # channel on the server, with the correct questions :)
    if channel:
        #print("Found channel...")
        messages = [message async for message in channel.history(limit=200)]
        q_msg = random.choice(messages)
        question_text = q_msg.content
        question_attachments = [await att.to_file() for att in q_msg.attachments]
        await ctx.send(question_text, files=question_attachments)
    else:
        question = "Sadly, I did not find the channel with the questions..."
        await ctx.send(question)

bot.run(os.getenv("TOKEN"))
