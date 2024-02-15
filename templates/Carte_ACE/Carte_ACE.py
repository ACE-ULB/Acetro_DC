import discord, sys
from discord.ext import commands

sys.path.append('modifier')
from Channel import *
from Permissions import *
sys.path.append('visualizer')
from Reaction import *
sys.path.append('text')
from Carte_ACE_text import *
from Emojis import *
sys.path.append('img')

from .Events import Events

TEMPLATES_NAME = 'Carte_ACE'

def get():
	return Carte_ACE

class Carte_ACE(commands.Cog, Events, name=TEMPLATES_NAME):

	def __init__(self, bot):
		self.bot = bot
		self.name = TEMPLATES_NAME

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		if not payload.member.bot:
			await self.switch_reaction(payload)

	@commands.Cog.listener()
	async def on_message(self, message):
		if not message.author.bot:
			await self.switch_message(message)

	async def initial_config(self, ctx):
		print("initial config")
		await lock_channel(ctx)
		logs = await create_channel(ctx, name='logs', topic=logs_topic)
		bdd_pwd = await create_channel(ctx, name='bdd_mdp', topic=bdd_pwd_topic)
		bdd_cartes = await create_channel(ctx, name='bdd_cartes', topic=bdd_cartes_topic)
		l_topic = [home_topic, logs_topic+" : "+str(logs.id), bdd_pwd_topic+" : "+str(bdd_pwd.id), bdd_cartes_topic+" : "+str(bdd_cartes.id)]
		await edit_topic(ctx, l_topic)
		img = discord.File("img/logos/ACE.png")
		welcome_msg = discord.Embed(title=wel_title, description=wel_description, thumbnail="attachment://img/logos/ACE.png", colour=0x000)
		await ctx.send(embed=welcome_msg)
		await self.init_setup_pwd(ctx)

	async def init_setup_pwd(self, ctx):
		msg = await ctx.send(txt_cmd_emojis['pause']+" "+wel_create_pwd)
		await msg.add_reaction(converter_text_to_emojis(txt_ctrl_emojis['valid'])[0])

		
