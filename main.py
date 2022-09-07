import discord
import random
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!",
                   help_command=None,
                   intents=discord.Intents.all(),
                   status=discord.Status.idle,
                   activity=discord.Activity(
                       type=discord.ActivityType.watching, name="Tonikawa"))

pics = [
    "https://imgur.com/8G85g1m", "https://imgur.com/VmlgHPj",
    "https://imgur.com/Ga713j1", "https://imgur.com/5Q5DqSv",
    "https://imgur.com/2EyUm74", "https://imgur.com/IgRC1sm",
    "https://imgur.com/0sxg2pE", "https://imgur.com/4Ej6uif",
    "https://imgur.com/e3lNPif", "https://imgur.com/B5BpvFL",
    "https://imgur.com/z4iaPSY", "https://imgur.com/zXDQvze"
]

quotes = [
    '"The greatest victory is that which requires no battle."',
    '"The wise warrior avoids the battle."',
    '"What the ancients called a clever fighter is one who not only wins, but excels in winning with ease."',
    '"He will win who knows when to fight and when not to fight."',
    '"Attack is the secret of defense; defense is the planning of an attack."',
    '"Wheels of justice grind slow but grind fine."',
    '"Opportunities multiply as they are seized."',
    '"To know your Enemy, you must become your Enemy."',
    '"know yourself and you will win all battles."',
    '"All warfare is based on deception."',
    '"The quality of decision is like the well-timed swoop of a falcon which enables it to strike and destroy its victim."',
    '"Let your rapidity be that of the wind, your compactness that of the forest."',
    '"Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt."'
]


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.command()
async def troll(ctx, member: discord.Member):
    if ctx.author.id==916700691718864986:
       with open("DATA", "r+") as f:
              f.truncate(0)
       with open("DATA", "a") as f:
              f.write(str(member.id))
       await ctx.channel.send(
                "https://tenor.com/view/ouro-kronii-we-do-a-little-trolling-hololive-gif-22976204")
    else:
       None
  
      
       
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(
        f"Welcome to the server {member.mention}! We hope you enjoy your stay.\n https://tenor.com/bQUMM.gif"
    )


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", colour=discord.Colour.blue())

    embed.set_image(url="https://i.imgur.com/NbQPk7k.png")
    embed.add_field(name="kick", value="!kick", inline=True)
    embed.add_field(name="ban", value="!ban", inline=True)
    embed.add_field(name="Delete messages", value="!clear", inline=True)
    embed.add_field(name="CUTE PICS", value="!pics", inline=True)
    embed.add_field(name="Summon", value="!summon", inline=True)
    embed.add_field(name="Quotes", value="!quote", inline=True)
    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    if message.content.startswith("!pics"):
        await message.channel.send(random.choice(pics))

    with open("DATA", "r") as f:
        v = int(f.read())

    if message.author.id == v:
        n = random.randint(1, 5)
        if n == 1:
            for i in range(1, 4):
                await message.channel.send(
                    "https://media.giphy.com/media/7yOlwaEK4RTs1fgi4j/giphy.gif"
                )
        elif n == 2:
            for i in range(1, 4):
                await message.channel.send(
                    "https://media.giphy.com/media/KShKGc5A5mnQKqB2AH/giphy.gif"
                )
        elif n == 3:
            for i in range(1, 4):
                await message.channel.send(
                    "https://media.giphy.com/media/7W0zp0j9obC04cYMil/giphy.gif"
                )
        elif n == 4:
            for i in range(1, 4):
                await message.channel.send(
                    "https://media.giphy.com/media/5veZnBmiUCZh29jRdZ/giphy.gif"
                )
    await bot.process_commands(message)


@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send(f"{member.mention} has been kicked")


@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.send(f"{member.mention} has been banned")


@bot.command()
async def summon(ctx, member: discord.Member):
    for i in range(0, 10):
        await ctx.channel.send(f"{member.mention}")


@bot.command()
async def quote(ctx):
    await ctx.channel.send(
        f"{random.choice(quotes)} – Sun Tzu, The Art of War.")


@bot.command()
async def stop(ctx):
    if ctx.author.id==916700691718864986:
      with open("DATA", "r+") as f:
          f.truncate(0)
      await ctx.channel.send("https://tenor.com/view/troll-gif-22102624")
      with open("DATA", "a") as f:
          f.write("1")


TOKEN = os.environ['TOKEN']
bot.run(TOKEN)
