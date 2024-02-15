import discord
from discord.ext import commands

async def echange_emoji_in_msg(message, from_change, to_change):
	ret = message.split(from_change)
	for idx in range(len(ret)):
		if ret[idx] == from_change:
			ret[idx] = to_change
	new_msg = ""
	for itr in ret : new_msg += itr
	return new_msg