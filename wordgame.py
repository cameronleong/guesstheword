# Word Game - github.com/cameronleong - 16/07/16 #
import discord
import random
import linecache
import re
import shelve
				
async def run(client, message):
	
	wordlistlines = 52794					#number of lines in the wordlist you're using
	distance = 0						#reset all the values
	winner = ''						
	left = "aardvark"					
	right = "zygote"
	
	linenumber = random.randint(0, wordlistlines)		#pick a random line number
	answer = linecache.getline('words.txt',linenumber)	#linecache allows you to pull a single line instead of the entire file
	answer = answer.replace('\n','')			#strip line breaks
	
	
	
	await client.send_message(message.channel, 'Guess the word between **'+left+'** and **'+right+'**!')
	while winner == '':
		guess = await client.wait_for_message(channel=message.channel)
		
		if guess.content.startswith("!") == True and guess.content == "!stop":
			fmt = 'Game Ended. It was **{}**.'
			await client.send_message(message.channel, fmt.format(answer))
			winner = "Game Stopped"
			break
			
		if guess.content.startswith("!") == True and guess.content == "!refresh":
			await client.send_message(message.channel, 'Guess the word between **'+left+'** and **'+right+'**!')
			
		if guess.content.startswith("!") == True and guess.content == "!hint":
			distance = await count_string(left,right)
			await client.send_message(message.channel, str(distance)+' known words are between **'+left+'** and **'+right+'**!')
			if distance < 200:
				await client.send_message(message.channel, 'The answer begins with **'+answer[0]+answer[1]+answer[2]+'**')
			#print(answer)				#cheat code here for debugging purposes	
			
		if guess.content.startswith("!") == True and guess.content == "!abc":
			await client.send_message(message.channel, 'a b c d e f g h i j k l m n o p q r s t u v w x y z')
					
		if guess.content.startswith("!") == False and guess.author != client.user:
			if guess.content == answer:
				await client.send_message(message.channel, 'You are right! The word is **{}**'.format(answer))
				winner = guess.author
				await client.send_message(message.channel, 'http://www.merriam-webster.com/dictionary/'+answer)
				break
			if guess.content != answer:
				if await check_string(guess.content):
					if left < guess.content and guess.content < right:
						if guess.content < answer:
							left = guess.content
							await client.send_message(message.channel, 'Guess the word between **'+left+'** and **'+right+'**!')
						else:
							right = guess.content
							await client.send_message(message.channel, 'Guess the word between **'+left+'** and **'+right+'**!')
				else:
					pass			#message was not a permitted word from the wordlist supplied
	
	
	if winner == 'Game Stopped':
		await client.send_message(message.channel, '\n:eggplant:  Everyone loses! :eggplant:')
	else:
		fmt = ':peach:  The winner is {} :peach:\n10 frickin dollarydoos have been awarded!'
		await client.send_message(message.channel, fmt.format(winner.mention))
		await addscore(client, message, winner)
	await client.send_message(message.channel, "\nType `!word` to start a new game or `!help` for instructions on how to play.")
	
	
async def check_string(w):
	if w.isalnum() and not (' ' in w):					
		with open("words.txt") as f:				#check if a user submitted word is found in the wordlist
			found = False
			#print('Iterating...')
			for line in f:  				#iterate over the file one line at a time(memory efficient)
				if re.match('{}$'.format(w),line):    	#if string found is in current line
					#print(line)
					return True
			if not found:
				#print('Not Found')
				return False
	else:
		return False

async def count_string(w,x):						#finds the distance between two words. used for !hint
	with open("words.txt") as myFile:
		for num, line in enumerate(myFile, 1):
			if re.match("{}$".format(w),line):
				leftnum = num
				#print("left num is "+str(leftnum))
				break
	with open("words.txt") as myFile:
		for num2, line in enumerate(myFile, 1):
			if re.match("{}$".format(x),line):
				rightnum = num2
				#print("right num is "+str(rightnum))
				return rightnum - leftnum -1
				
async def addscore(client, message, user):
	score = shelve.open('leaderboard', writeback=True)
	if user.id in score:
		current = score[user.id]
		score[user.id] = current + 10
	else:
		score[user.id] = 10
	await client.send_message(message.channel, str(user.name)+" now has "+str(score[user.id])+" dollarydoos")
	score.sync()
	score.close()
	
async def scoreboard(client,message):
	counter = 0
	scoreStr= "\n         :star: Top 10 Players :star: \n\n"
	score = shelve.open('leaderboard')
	klist = score.keys()
	scoreboard = {}
	for key in klist:
		m = discord.utils.get(message.server.members, id=key)
		scoreboard[m.name] = score[key]
	
	for item in sorted(scoreboard, key=scoreboard.get, reverse=True):
		if counter < 10:
			scoreStr += ':military_medal: `{:20}{:>4}`\n'.format(str(item),str(scoreboard[item]))
			counter = counter + 1
	await client.send_message(message.channel,scoreStr)
	score.close()				
