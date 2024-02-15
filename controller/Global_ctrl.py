import discord, datetime
from discord.ext import commands

def get_time_formated(datetime):
	return datetime.strftime("%d/%m/%Y - %H:%M+01:00")
	
def get_channel_id_in_topic(channel, search):
	topic = channel.topic
	topic = topic.split('\n')
	ret = None
	for txt in topic:
		if search in txt:
			ret = txt[len(search)+len(" : "):]
	return int(ret)

async def get_message_with_id(bot, c_id, m_id):
	channel = await bot.fetch_channel(c_id)
	message = await channel.fetch_message(m_id)
	return message