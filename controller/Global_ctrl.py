import discord
from discord.ext import commands

def get_channel_id_in_topic(channel, search):
	topic = channel.topic
	topic = topic.split('\n')
	ret = None
	for txt in topic:
		if search in txt:
			ret = txt[len(search)+len(" : "):]
	return int(ret)