import discord
from discord.ext import commands

import sys

class Head(commands.Cog, name='Head'):
	
	def set_templates(self, temp):
		self.templates = temp

	@commands.command(name="discord")
	async def g_exist(self, ctx):
		print("scord")
		await ctx.send("scord")

	@commands.command(name="clear") #developpers
	async def clear_test(self, ctx):
		print("cleaning")
		if ctx.author.guild_permissions.administrator:
			for chan in ctx.channel.category.text_channels:
				if chan != ctx.channel:
					await chan.delete()
			await ctx.send("Cleaned ! :D")

	@commands.command(name="carte_ace")
	async def init_config(self, ctx):
		print("Starting config Carte ACE setup")
		inst = self.templates['Carte_ACE']
		await inst.initial_config(ctx)