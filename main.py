import discord
import random
from discord.ext import commands
import os

token = os.environ.get("TECH_AND_GAMING_BOT")

client = commands.Bot(command_prefix = ",")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")

@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for banned_entry in banned_users:
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return

client.run(token)        
