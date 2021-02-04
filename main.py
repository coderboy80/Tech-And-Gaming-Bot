import discord
import random
from discord.ext import commands
import os

token = os.environ.get("TECH_AND_GAMING_BOT")

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is ready")



@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}\nReason={reason}")

@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for banned_entry in banned_user:
        user = banned_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return
        
@client.command(aliases=["p"])
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")

@client.command(aliases=["purge"])
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}\nReason={reason}")

@client.command(alaises=["hi"])
async def hello(ctx):
    await ctx.send(f"Hello!")

client.run(token)        
