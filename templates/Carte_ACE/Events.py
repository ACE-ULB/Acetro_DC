import discord, sys
from discord.ext import commands

sys.path.append('visualizer')
from Reaction import *
sys.path.append('controller')
from Carte_ACE_ctrl import *
from Global_ctrl import *
sys.path.append('text')
from Carte_ACE_text import *
from Emojis import *

class Events:

	async def switch_reaction(self, payload):
		message = await self.get_message_got_reaction(payload)
		if (wel_create_pwd in message.content) and (payload.emoji.name == converter_text_to_emojis(txt_ctrl_emojis['valid'])[0]):
			await self.setup_bdd_pwd(message)

	async def switch_message(self, message):
		pass

	async def get_message_got_reaction(self, payload):
		chan = self.bot.get_channel(payload.channel_id)
		msg = await chan.fetch_message(payload.message_id)
		return msg

	async def setup_bdd_pwd(self, message):
		list_pwd = create_password_cercles()
		bdd_channel_id = get_channel_id_in_topic(message.channel, bdd_pwd_topic)
		bdd_channel = self.bot.get_channel(bdd_channel_id)
		data = ""
		for idx in list_pwd:
			if (len(data) + len(idx[0]+" = "+idx[1]+"\n")) < 2000:
				data = data + idx[0] + " = " + idx[1] + "\n"
			else: 
				print("Out of Range")
		await bdd_channel.send(data)