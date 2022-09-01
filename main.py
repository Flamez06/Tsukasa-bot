import discord
import random
import os
from discord.ext import commands

# intents = discord.Intents.default()
# intents.message_content = True
#client = discord.Client(intents = discord.Intents.all())
bot = commands.Bot(command_prefix="!",intents = discord.Intents.all(),status=discord.Status.idle,activity = discord.Activity(type=discord.ActivityType.watching, name="Tonikawa"))

pics = ["https://imgur.com/8G85g1m", "https://imgur.com/VmlgHPj", "https://imgur.com/Ga713j1", "https://imgur.com/5Q5DqSv", "https://imgur.com/2EyUm74",
        "https://imgur.com/IgRC1sm", "https://imgur.com/0sxg2pE", "https://imgur.com/4Ej6uif", "https://imgur.com/e3lNPif", "https://imgur.com/B5BpvFL"]

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
  
@bot.event
async def on_member_join(member):
  channel = bot.get_channel(927467027378110536)
  await channel.send(f"Welcome to the server {member.mention}! We hope you enjoy your stay.\n https://tenor.com/bQUMM.gif")

@bot.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    if message.content.startswith("!pics"):
      await message.channel.send(random.choice(pics))
        
    if message.author.id==719779948348309594:
      n=random.randint(1,5)
      if n==1:
        for i in range(1,4):
          await message.channel.send("https://media.giphy.com/media/7yOlwaEK4RTs1fgi4j/giphy.gif")
      elif n==2:
        for i in range(1,4):
          await message.channel.send("https://media.giphy.com/media/KShKGc5A5mnQKqB2AH/giphy.gif")
      elif n==3:
        for i in range(1,4):
          await message.channel.send("https://media.giphy.com/media/7W0zp0j9obC04cYMil/giphy.gif")
      elif n==4:
        for i in range(1,4):
          await message.channel.send("https://media.giphy.com/media/5veZnBmiUCZh29jRdZ/giphy.gif")
    await bot.process_commands(message)
  
@bot.command()
async def kick(ctx, member:discord.Member,*,reason=None):
  await member.kick(reason=reason)
  await ctx.channel.send(f"{member.mention} has been kicked")

@bot.command()
async def clear(ctx,amount=5):
  await ctx.channel.purge(limit=amount)

@bot.command()
async def ban(ctx,member:discord.Member,*,reason=None):
  await member.ban(reason=reason)
  await ctx.channel.send(f"{member.mention} has been banned")

  
TOKEN = os.environ['TOKEN']
bot.run(TOKEN)
