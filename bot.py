import praw
import os
import re
import pymongo
from cowpy import cow

''' Compile the pattern we use to find cowbot directives. '''
directive=re.compile('@cowbot(:(?P<actor>[A-Za-z]+))?')

''' Define the user-agent for this bot, as well as a link to our codebase. '''
agent='[```cowbot/1.0```](https://github.com/msoliter/cowbot)'

''' Log us in and set up the 'r' reddit object for global use. '''
r = praw.Reddit(user_agent=agent)
r.login('cowb0t', os.environ.get('BOT_PASSWORD'))

''' Set up a Mongo client for tracking what we've already responded to. '''
m = pymongo.MongoClient(host = os.environ.get('MONGO_URI'))
comments_collection = m['CloudFoundry_qrekuir3_aqa6ptqp']['comments']

def indent(message, size=4, delimiter='\n'):
  ''' Indents a message by `size spaces. '''
  return delimiter.join(
    map(
      lambda line: (' ' * size) + line, 
      message.split(delimiter)))

def sign(message):
  ''' Signs a string message with a signature from this bot. '''
  return message + '\n\n^' + agent

def get_parent_content(comment):
  ''' Retrieves the content of whatever this comments parent is. '''
  parent = r.get_info(thing_id=comment.parent_id)
  return parent.selftext if type(parent) is praw.objects.Submission else parent.body
  
if __name__ == '__main__':
  for comment in praw.helpers.comment_stream(r, 'all', verbosity=0):
    match = directive.search(comment.body)

    if match:
      id = comment.id
      document = {'_id': id}
      
      if comments_collection.find_one(document):
        continue

      content = get_parent_content(comment)
      actor_name = match.group('actor')
      
      if actor_name:
        actor = cow.get_cow(actor_name.strip())
        actor = None if actor == 'default' else actor()    
      else:
        actor = None
      
      if type(actor) is not str and actor is not None:
        message = actor.milk(content)
      else:
        message = cow.milk_random_cow(content)
      
      comment.reply(sign(indent(message)))
      comments_collection.insert(document)

