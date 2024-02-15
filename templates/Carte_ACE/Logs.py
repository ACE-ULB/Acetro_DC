import discord, sys
from discord.ext import commands

sys.path.append('controller')
from Global_ctrl import *
sys.path.append('text')
from Carte_ACE_text import *

class Logs:

	async def switch_logs(self, ctx, event, status):
		if event == 'initial_config':
			title = "Initialisation de l'espace Carte ACE"
		elif event == 'init_bdd_pwd':
			title = "Création des mots de passe pour les comptes des gestionnaires"
		else:
			title = "Opération inconnue ???"
		log_chan = await self.get_logs_channel(ctx)
		msg = await self.log_message(ctx, title, status)
		await log_chan.send(embed=msg)

	async def log_message(self, ctx: discord.ext.commands.context.Context, title, status):
		message = discord.Embed(title=title, color=self.get_color_status(status), description="Author : "+ctx.author.mention)
		message.set_footer(text=get_time_formated(ctx.message.created_at))
		message.set_thumbnail(url=ctx.author.avatar.url)
		return message

	async def log_message(self, ctx: discord.RawReactionActionEvent, title, status):
		message = discord.Embed(title=title, color=self.get_color_status(status), description="Author : "+ctx.member.mention)
		og_msg = await get_message_with_id(self.bot, ctx.channel_id, ctx.message_id)
		message.set_footer(text=get_time_formated(og_msg.created_at))
		message.set_thumbnail(url=ctx.member.avatar.url)
		return message

	def get_logs_channel(self, ctx: discord.ext.commands.Context):
		logs_channel_id = get_channel_id_in_topic(ctx.channel, logs_topic)
		logs_channel = self.bot.get_channel(logs_channel_id)
		return logs_channel

	async def get_logs_channel(self, ctx: discord.RawReactionActionEvent):
		og_msg = await get_message_with_id(self.bot, ctx.channel_id, ctx.message_id)
		logs_channel_id = get_channel_id_in_topic(og_msg.channel, logs_topic)
		logs_channel = self.bot.get_channel(logs_channel_id)
		return logs_channel

	def get_color_status(self, status):
		if status == 'success':
			return 0x15f00e
		elif status == 'failure':
			return 0xfa0707
		else:
			return 0x000