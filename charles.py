import discord
import random
import linecache
import re
import shelve
from wordgame import *

client = discord.Client()
busyChannels = []
#game = discord.Game(name="github.com/cameronleong", url="github.com/cameronleong")

@client.event
async def on_message(message):
	if message.author == client.user:			# we do not want the bot to reply to itself
		return
		
	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
	
	if message.content.startswith('!word'):
		if message.channel in busyChannels:
			await client.send_message(message.channel, "Channel busy with another activity.")
		else:
			busyChannels.append(message.channel)
			await client.send_message(message.channel, "Starting **Guess-the-Word** in `#"+message.channel.name+"`...")
			await run(client, message)
			busyChannels.remove(message.channel)
			
	if message.content.startswith('!score'):
		await scoreboard(client, message)

	if message.content.startswith('!help'):
		await client.send_message(message.author, '```Guess the Word```\n*Written by mm#4317 in Python 3 using the discordpy API library by https://github.com/Rapptz*\n\nThe objective of this game is to guess a randomly chosen word by narrowing it down between two alphabetically-sorted bounds. The bounds always start from the first and last words in the bot\'s dictionary: **aardvark** and **zygote**.\n ```An Example```\nFor instance, if the word chosen is **credible** then typing in **cat** will prompt the bot to respond with\n\n`Guess the word between **cat** and **zygote**`\n\nsince credible is between cat and zygote (but not aardvark and cat). Following that logic, typing in **dog** will prompt the response\n\n`Guess the word between **cat** and **dog**`.\n\nTake note that alphabetical order means that words like "catastrophe" and "dane" are valid words that are between **cat** and **dog** while words like "cab" aren\'t (both cata... and d... are after cat but cab is before c-a-t).\n ```Commands``` \n `!word` - Starts a game of Guess the Word\n `!help` - Displays this page\n `!abc`  - Lists the english alphabet for your convenience\n `!hint` - Reveals first three letters once there are less than 200 words left\n `!stop` - Stops an ongoing game\n `!score` - Displays the top five players\n ```Shoutouts``` \nSpecial thanks to Gene, route6x, rebornZ, Krypt, bry, hedwig, pan, drk, Acel and all the chumps at GTFOs discord server for helping me test the game. Seeing everyone have fun for hours and hours on end has been a huge motivation for me- I hope you have enjoyed watching the bot grow as much as I have.\n ```Contact``` \n https://github.com/cameronleong')


		
@client.event
async def on_ready():
	print('Connected!')
	print('Username: ' + client.user.name)
	print('ID: ' + client.user.id)
	#await client.change_status(game)
	

client.run('YOUR TOKEN HERE')
