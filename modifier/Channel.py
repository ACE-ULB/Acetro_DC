import discord
from discord.ext import commands

from Permissions import *

async def edit_topic(ctx, content=list()):
	topic=""
	for txt in content:
		topic = topic + txt + "\n"
	await ctx.channel.edit(topic=topic)

async def create_channel(ctx, name, topic):
	channel = await ctx.channel.category.create_text_channel(name, topic=topic)
	await lock_channel(ctx)
	return channel