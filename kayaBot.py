from random import random
import discord as dc
from discord.ext.commands import Bot
from discord.ext import commands
from discord.embeds import Embed
import random
intents = dc.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents= intents)
token = "MTA2MzgzNDU0ODE5MTg5NTcwNQ.Gj6gPg.RDOh3b2TFEZb1fq8-F8S71jM77EzehR0nZROcE"
# client = dc.Client(intents= dc.Intents.default())
@client.command(pass_context = True)
async def ping(ctx):
    await ctx.channel.send(ctx.guild)
    await ctx.channel.send(ctx.author.mention)
    await ctx.channel.send("Pong")
    print("Worked")

@client.command()
async def slap(ctx):
    embed = dc.Embed(
        colour=(dc.Colour.random()), description= f"({ctx.author.mention} Punches you!!)"
    )
    embed.set_image(url=slap[0])
    await ctx.channel.send(embed = embed)

@client.event
async def on_ready():
    print('Bot is logging in as: {0.user}'.format(client))

@client.listen('on_message')
async def on_message(message):
    if(message.author == client.user):
        return
    if(message.content.startswith('Kaya')):
        await message.channel.send('HELLO!!! {0.user}'.format(client))
    # await client.process_command(message) 


client.run(token= token)

#420907117632

slap =  [
            'https://tenor.com/view/slap-christmas-gif-24241359',
            'https://tenor.com/view/slap-in-the-face-slap-hit-ouch-anger-gif-17283089',
            'https://tenor.com/view/slapping-cat-slap-slap-kiss-gif-7202286',
            'https://tenor.com/view/sasha-banks-smack-down-womens-champion-spider-man-slap-slaps-gif-22796795'
        ]

horn =  [
            'https://tenor.com/view/horny-gif-18480187',

        ]
olive = [
            'https://tenor.com/view/olive-you-olives-bear-dancing-love-gif-11851625'
        ]