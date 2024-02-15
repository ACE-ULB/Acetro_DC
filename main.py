import os
import sys
from importlib import import_module
from importlib.util import find_spec
from pkgutil import walk_packages
from dotenv import load_dotenv
import discord
from discord.ext import commands

#CLASS IMPORT
from Head import Head

#OTHER IMPORT
sys.path.append('utils')
from resolver import metaclass_resolver as m_r

#LOAD BOT TOKEN in .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def metaclass():
	pass

class HeadEmbed(m_r(commands.Bot, Head)):
	
	async def on_ready(self):
		print("========================================================")
		print(bot.user.name, "has connected to Discord Bot API !")
		print("He's connected to", len(bot.guilds), "servers")
		print("========================================================")
		print("\nLogs : ")

	async def on_command_error(self, ctx, error):
		print(ctx)
		print(error)

#ALL TEMPLATES IMPORT FUNCTION
def import_templates(package, recursive=True):
	if isinstance(package, str):
		package = import_module(package)
	results = {}
	for loader, name, is_pkg in walk_packages(package.__path__):
		full_name = package.__name__ + '.' + name
		results[name] = import_module(full_name)
		if recursive and is_pkg:
			results.update(import_templates(full_name))
	return results


#MAIN
if __name__ == '__main__':
	#SEND TO DISCORD API WHAT I LOOK = Intents
	intents = discord.Intents().all()

	#LOAD HeadEmbed BOT
	bot = HeadEmbed(command_prefix='-', intents=intents)

	#IMPORT ALL TEMPLATES
	templates = {}
	tmp = import_templates("templates")
	for tem in tmp:
		try:
			templates[tem] = tmp[tem].get()
			bot.add_cog(templates[tem](bot))
			templates[tem] = bot.get_cog(tem)
		except(AttributeError):
			pass

	#ADD COMMAND Head
	bot.add_cog(Head(bot))
	Head = bot.get_cog('Head')
	print(templates)
	Head.set_templates(templates)

	#RUN BOT
	bot.run(TOKEN)