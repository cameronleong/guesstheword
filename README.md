# Guess the Word Discord Bot
Discord bot built using discord.py library.

# Requirements
-Python 3.5

-pip  
https://pip.pypa.io/en/stable/installing

-discord.py  
https://github.com/Rapptz/discord.py  
`python3 -pip install -U discord.py`  

# Help

The objective of this game is to guess a randomly chosen word by narrowing it down between two alphabetically-sorted bounds. The bounds always start from the first and last words in the bot's dictionary: **aardvark** and **zygote**.

For instance, if the word chosen is **credible** then typing in **cat** will prompt the bot to respond with  

`Guess the word between **cat** and **zygote**`  

since credible is between cat and zygote (but not aardvark and cat). Following that logic, typing in **dog** will prompt the response

`Guess the word between **cat** and **dog**`. 

Take note that alphabetical order means that words like "catastrophe" and "dane" are valid words that are between **cat** and **dog** while words like "cab" aren't (both cata... and d... are after cat but cab is before c-a-t).

**Commands**  
`!word` - Starts a game of Guess the Word  
`!help` - Displays this page  
`!abc`  - Lists the english alphabet for your convenience  
`!hint` - Reveals first three letters once there are less than 200 words left  
`!stop` - Stops an ongoing game  
`!score` - Displays the top five players  




