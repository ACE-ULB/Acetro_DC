import discord
from discord.ext import commands

async def lock_channel(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False, add_reactions=False, external_emojis=False)

def get_everyone_role(ctx):
    return ctx.guild.default_role

def get_author(ctx):
    return ctx.message.author
    