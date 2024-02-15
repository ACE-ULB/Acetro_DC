import discord
from discord.ext import commands
import string, random, os

def password_generator(list_to_assign):
	list_to_return = list()
	all_characters = string.ascii_letters + string.digits + string.punctuation
	length = 13
	for idx in list_to_assign:
		password = ''.join(random.choices(all_characters, k=length))
		list_to_return.append((idx, password))
	return list_to_return

def create_password_cercles():
	list_cercles = os.listdir("img/logos/")
	for i in range(len(list_cercles)): list_cercles[i] = list_cercles[i].split('.')[0]
	tuple_cercle_pwd = password_generator(list_cercles)
	return tuple_cercle_pwd