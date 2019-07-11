import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!bot'):
        msg = 'Have You Called Me :thinking:  {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
       
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('8ball Pool Ready to Go!')

client.run('TOKEN')