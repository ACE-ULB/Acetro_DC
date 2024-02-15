import discord, emojis
from discord.ext import commands

def converter_text_to_emojis(text):
		switcher = {
			list: text,
			str: [text]
		}
		text = switcher.get(type(text), TypeError)
		emoret = list()
		for emotxt in text:
			tmp = emojis.encode(emotxt)
			emoret.append(tmp)
		return emoret

async def add_reaction(message, emoji):
	await message.add_reaction(emoji)

async def add_multi_reactions(message, emojis):
	for emoji in emojis:
		await message.add_reaction(emoji)

async def remove_all_reactions(message):
	await message.clear_reactions

async def remove_reaction(message, emoji):
	await message.clear_reaction(emoji)