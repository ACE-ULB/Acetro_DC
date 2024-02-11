import discord, sys
from discord.ext import commands

import sys

TEMPLATES_NAME = 'Carte_ACE'

def get():
	return Carte_ACE

class Carte_ACE(commands.Cog, name=TEMPLATES_NAME):

	def __init__(self, bot):
		self.bot = bot
		self.name = TEMPLATES_NAME