import discord
from discord.ext import commands
import Game
import Bot
import random
import asyncio
import aiohttp
import json

client = discord.Client()

# hello

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('8ball hello'):
        await message.channel.send('Hello :wink: {0.author.mention}'.format(message))
         
        
# bot 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('8ball bot'):
        await message.channel.send('You Called Me :thinking: {0.author.mention}'.format(message))
      
# 8ball

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))
   
@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate']
       
   
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('8ball Pool Ready to Go!')

client.run('TOKEN')