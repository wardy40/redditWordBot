# bigwordbot

import praw
from PyDictionary import PyDictionary
import enchant

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id= 'dtB2Q9bTVA2k1w',
					 client_secret='KPgxTHpClWGCUCfh3IgXF-vuzt6OcQ',
					 username='testbot',
					 password='testbot',
					 user_agent='testbot')

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('rentastreamer')

# phrase to activate the bot
keyphrase = '!wordbot'

# dictionary and word check
dictionary = PyDictionary()
d = enchant.Dict("en_US")

def isWord(word):
	return d.check(word)

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
	if keyphrase in comment.body:
		word = comment.body.replace(keyphrase, '')
		try:
			if isWord(word):
				# get meaning as object, get the index of a sentence and reply its definition
				words = dictionary.meaning(word)
				reply = [item[0] for item in words.values()]
				comment.reply(word + ': ' + reply[0])
				print('posted')
			else:
				reply = 'This is not a word.'
				comment.reply(reply)
				print('posted')
		except:
			print('too frequent')
			