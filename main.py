import discord
import os

#Create connection to compile
client = discord.Client()


#Async even for when we log in
@client.event
async def on_ready():  #this name comes from discord.py lib
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return #We dont react to messages we write

  if message.content.startswith('$greet'):
    await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))